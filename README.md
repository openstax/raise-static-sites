# RAISE Static Sites

This repository contains the code and configuration used to generate sites for RAISE content which are hosted outside of Moodle. The repo uses [Hugo](https://gohugo.io/) to generate either student or teacher facing site content.

## Development

Developers will need to install Hugo. OS specific instructions can be found [here](https://gohugo.io/installation/).

The Hugo webserver can be used to preview content in a local dev environment:

```bash
$ hugo server -e students # Use -e teachers for teacher content
```

The output of the command will provide a local URL / port to access (typically [http://localhost:1313/](http://localhost:1313/)).

## Generating static content

Content can be generated to `./public` using the `Hugo` CLI:

```bash
$ rm -rf ./public # Cleanup existing files
$ hugo -e students # Use -e teachers for teacher content
```

## Creating files for a new edition

The repo includes utility Python scripts that can be used to generate files for a new edition. Both scripts expect the CSV output generated from [generate-mbz-toc](https://github.com/openstax/raise-mbtools/blob/main/mbtools/generate_mbz_toc.py).

```bash
$ pip install -r ./scripts/requirements.txt
$ python ./scripts/generate_content.py {path to ToC CSV} students ./content/students/{edition}/.
$ python ./scripts/generate_content.py {path to ToC CSV} teachers ./content/teachers/{edition}/.
$ python ./scripts/generate_toc.py {path to ToC CSV} students ./data/students/{edition}/toc.json
$ python ./scripts/generate_toc.py {path to ToC CSV} teachers ./data/teachers/{edition}/toc.json
```
