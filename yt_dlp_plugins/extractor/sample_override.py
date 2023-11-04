from yt_dlp.extractor.youtube import YoutubeIE

# ⚠ Other plugins cannot be overridden using this method
# ⚠ The extractor internals may change without warning, breaking the plugin



class _SampleOverridePluginIE(YoutubeIE, plugin_name='sample'):
    def _real_extract(self, url):
        self.to_screen('Passing through SampleOverridePluginIE')
        return super()._real_extract(url)
