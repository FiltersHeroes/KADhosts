#!/usr/bin/env python3
# coding=utf-8
# pylint: disable=C0103
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# Is it online?
"""MIT License

Copyright (c) 2023 Filters Heroes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
import os
import re
import asyncio
import dns.asyncresolver
from dns.resolver import NoNameservers, NXDOMAIN, NoAnswer, Timeout, NoResolverConfiguration
import git


pj = os.path.join
pn = os.path.normpath

script_path = os.path.dirname(os.path.realpath(__file__))

git_repo = git.Repo(script_path, search_parent_directories=True)
# Main_path is where the root of the repository is located
main_path = git_repo.git.rev_parse("--show-toplevel")


PAGE_HOSTS_PAT = re.compile(r"^.*?\d+\.\d+\.\d+\.\d+ (.*)")
pages = []
with open(pj(main_path, "KADhosts.txt"), "r", encoding="utf-8") as kh:
    for line in kh:
        if match_h := PAGE_HOSTS_PAT.match(line):
            pages.append(match_h.group(1))

WWW_PAT = re.compile(r"^(www[0-9]\.|www\.)")
for i, page in enumerate(pages):
    pages[i] = re.sub(WWW_PAT, "", page, count=1)

pages = sorted(set(pages))

sem_value = 10
exclusions_path = pj(main_path, "exclusions")

my_resolver = dns.asyncresolver.Resolver()
my_resolver.nameservers = ['1.1.1.1', '1.0.0.1']

async def domain_dns_check(domain, limit):
    async with limit:
        status = "online"
        try:
            print("Checking the status of domains...")
            await my_resolver.resolve(domain)
        except (NXDOMAIN, Timeout, NoAnswer, NoNameservers) as ex:
            print(ex)
            status = "offline"
        except (NoResolverConfiguration) as ex:
            print(ex)
        finally:
            result = f"{domain} {status}"
    return result


async def bulk_domain_dns_check(limit_value):
    limit = asyncio.Semaphore(limit_value)
    entries = await asyncio.gather(*[domain_dns_check(domain, limit) for domain in pages])
    if not os.path.exists(exclusions_path):
        os.mkdir(exclusions_path)
    with open(pj(exclusions_path, "offline.txt"), "w", encoding="utf-8") as offline_f:
        for result in entries:
            splitted_result = result.split()
            if splitted_result[1] == "offline":
                offline_f.write(f"{splitted_result[0]}\n")

asyncio.run(bulk_domain_dns_check(sem_value))

with open(pj(exclusions_path, "offline.txt"), "r", encoding="utf-8") as fp:
    num_lines = sum(1 for line in fp if line.rstrip())
    print('Total offline domains:', num_lines)
