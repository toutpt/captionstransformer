from captionstransformer import transcript, ttml, sbv, srt

REGISTRY = {'transcript':{'reader': transcript.Reader,
                          'writer': transcript.Writer,
                          'mimetype': 'text/xml',
                          'extension': '.xml'},
            'TTML':{'reader': ttml.Reader,
                    'writer': ttml.Writer,
                    'mimetype': 'application/ttml+xml',
                    'extension': '.xml'},
            'SBV': {'reader': sbv.Reader,
                    'writer': sbv.Writer,
                    'mimetype': 'text/plain',
                    'extension': '.sbv'},
            'SRT': {'reader': srt.Reader,
                    'writer': srt.Writer,
                    'mimetype': 'text/plain',
                    'extension': '.srt'}}
