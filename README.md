## YouTube OAuth2 for yt-dlp

This repository contains a plugin package that adds support for logging into YouTube with OAuth2 to [yt-dlp's](https://github.com/yt-dlp/yt-dlp#readme) YouTube Extractors. 

Please note: This is experimental and may break at any time.

## Installation

Requires yt-dlp `2023.10.13` or above.

You can install this package with pip:
```
python3 -m pip install -U https://github.com/coletdjnz/yt-dlp-youtube-oauth2/archive/master.zip
```

See [installing yt-dlp plugins](https://github.com/yt-dlp/yt-dlp#installing-plugins) for the other methods this plugin package can be installed.

## Usage

Enable oauth with `--extractor-args youtube:oauth`.

On first run you will be prompted to authorize yt-dlp to access your YouTube account.
> [youtube+oauth] Please visit  https://www.google.com/device  and enter code XXXX-YYYY

Open the link in your browser and enter the code. It will say the request is for YouTube on TV - this is normal, as we are using the YouTube on TV client for oauth ;)

The token data is saved in the yt-dlp cache.

Note: avoid running with YouTube cookies, as it may cause issues.