# PyCon TW Archived Websites

The resting place for historical PyCon TW websites.

In order to better preserve things, we crawl each year's PyCon TW website into static HTML after the conference ends. The static websites are served on GitHub Page and the requests for historical websites are proxied from `tw.pycon.org` to GitHub Page with [pycontw-nginx](https://github.com/pycontw/pycontw-nginx). See the crawling script on `main` branch and the archived HTML on `gh-pages` branch.

## Usage

- Installing dependencies

  ```bash
  pipenv install
  ```

- To scrap a specific PyCon TW website, insert the command

  ```bash
  pipenv run python main.py -y [YEAR] --base [BASE]
  ```

  where `YEAR` should be the path of website (e.g. `2020` for `https://tw.pycon.org/2020`) and `BASE` for the base URL or base path used in the static HTML.

- To serve scraped static pages on your local machine, run the command:

  ```bash
  python -m http.server --cgi [PORT]
  ```

  and then access `localhost:[PORT]`.

  or run the command:

  ```bash
  pipenv run serve
  ```

  and access `localhost:5000`.