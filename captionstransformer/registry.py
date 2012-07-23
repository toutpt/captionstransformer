from captionstransformer import transcript, ttml, sbv, srt

REGISTRY = {'transcript':{'reader': transcript.Reader,
                    'writer': transcript.Writer},
            'TTML':{'reader': ttml.Reader,
                    'writer': ttml.Writer},
            'SBV': {'reader': sbv.Reader,
                    'writer': sbv.Writer},
            'SRT': {'reader': srt.Reader,
                    'writer': srt.Writer}}
