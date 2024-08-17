## YouTube OAuth2 for yt-dlp

This repository contains a plugin package that adds support for logging into YouTube with OAuth2 to [yt-dlp's](https://github.com/yt-dlp/yt-dlp#readme) YouTube Extractors. 

Please note: **This is experimental and may break at any time!!**.

For general plugin support, please see the yt-dlp discord server as responses may be slow here.

## Installation

Requires yt-dlp `2024.08.XX` or above.

If yt-dlp is installed through `pip` or `pipx`, you can install the plugin with the following:

pip:
```
python3 -m pip install -U https://github.com/coletdjnz/yt-dlp-youtube-oauth2/archive/refs/heads/master.zip
```

pipx:
```
pipx inject yt-dlp https://github.com/coletdjnz/yt-dlp-youtube-oauth2/archive/refs/heads/master.zip
```

If you have not installed yt-dlp through pip or pipx, see [installing yt-dlp plugins](https://github.com/yt-dlp/yt-dlp#installing-plugins) for the other methods this plugin package can be installed.

## Usage

### Enabling
Enable logging in with OAuth2 with `--username oauth2 --password ''`. You can add this to your [yt-dlp config file](https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#configuration)

Alternatively, if you only want to apply this for the YouTube extractor, you can add the following to a [.netrc file](https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#authentication-with-netrc):
 ```
machine youtube login oauth2 password ""
```

### Logging in 
On first run you will be prompted to authorize yt-dlp to access your YouTube account.
> [youtube+oauth2] To give yt-dlp access to your account, go to  https://www.google.com/device  and enter code XXX-YYY-ZZZ

Open the link in your browser and enter the code. It will say the request is for YouTube on TV - this is normal, as we are using the YouTube on TV client for oauth ;)

The token data is saved in the yt-dlp cache.

If you encounter issues, run yt-dlp with verbose logging (`-v`). If you see `Loading youtube-oauth2.token_data from cache`, then it should be trying to use oauth.

Note: avoid running with YouTube cookies, as it may cause issues.
