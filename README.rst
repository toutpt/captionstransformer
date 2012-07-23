Introduction
============

This package is a set of tools to transform captions from one format to another.
You will find Writer and Reader for each format and a script if you want
to use it in command line.

Supported Format:

* sbv Reader and Writer
* srt Reader and Writer
* ttml Reader and Writer
* transcript Reader and Writer

How to use (API)
================

You can read the provided unittest to have complete examples.

    from captionstransformer.sbv import Reader
    from captionstransformer.ttml import Writer
    from StringIO import StringIO
    test_content = StringIO(u"""
    0:00:03.490,0:00:07.430
    >> FISHER: All right. So, let's begin.
    This session is: Going Social
    
    0:00:07.430,0:00:11.600
    with the YouTube APIs. I am
    Jeff Fisher,
    
    0:00:11.600,0:00:14.009
    and this is Johann Hartmann,
    we're presenting today.
    
    0:00:14.009,0:00:15.889
    [pause]
    """)
    reader = Reader(test_content)

    captions = reader.read()
    len(captions) == 4
    first = captions[0]
    type(first.text) == unicode
    first.text == u">> FISHER: All right. So, let's begin.\nThis session is: Going Social\n"

    # next get a writer
    filelike = StringIO()
    writer = Writer(filelike)
    writer.set_captions(captions)
    text = writer.captions_to_text()
    text.startswith(u"""<tt xml:lang="" xmlns="http://www.w3.org/ns/ttml"><body><div>""")
    writer.write()
    writer.close()

About Formats
=============

This quite hard to find simple documentation about existing caption format.
Here is a set of existing named caption format:

SubViewer (*.SUB)::

    00:04:35.03,00:04:38.82
    Hello guys... please sit down...
    
    00:05:00.19,00:05:03.47
    M. Franklin,[br]are you crazy?


Youtube (SBV)::

    0:00:03.490,0:00:07.430
    FISHER: All right. So, let's begin.
    This session is: Going Social
    
    0:00:07.430,0:00:11.600
    with the YouTube APIs. I am
    Jeff Fisher,
    
    0:00:11.600,0:00:14.009
    and this is Johann Hartmann,
    we're presenting today.
    
    0:00:14.009,0:00:15.889
    [pause]

SubRip (.srt)::

    1
    00:00:03,490 --> 00:00:07,430
    FISHER: All right. So, let's begin.
    This session is: Going Social
    
    00:00:07,430 --> 00:00:11,600
    with the YouTube APIs. I am
    Jeff Fisher,
    
    2
    00:00:11,600 --> 00:00:14,009
    and this is Johann Hartmann,
    we're presenting today.
    
    3
    00:00:14,009 --> 00:00:15,889
    [pause]

Timed Text Markup Language (TTML)::

    <tt xml:lang="" xmlns="http://www.w3.org/ns/ttml">
      <body region="subtitleArea">
        <div>
          <p xml:id="subtitle1" begin="0.76s" end="3.45s">
            It seems a paradox, does it not,
          </p>
          <p xml:id="subtitle2" begin="5.0s" end="10.0s">
            that the image formed on<br/>
            the Retina should be inverted?
          </p>
        </div>
      </body>
    </tt>

Returned by http://video.google.com/timedtext?lang=en&v=VIDEOID ::

    <?xml version="1.0" encoding="utf-8" ?>
    <transcript>
        <text start="10" dur="2">Hi, I&amp;#39;m Emily from Nomensa</text>
        <text start="12" dur="3">and today I&amp;#39;m going to be talking about the order of content on your pages.</text>
        <text start="16" dur="6">Making sure the content on your web pages is presented logically is a really important part of web accessibility.</text>
        <text start="23" dur="2">Page content should be ordered so it makes sense</text>
    </transcript>


Microsoft SAMI (.sami, .smi)::

    <SAMI>
    <Head>
       <Title>President John F. Kennedy Speech</Title>
       <SAMIParam>
          Copyright {(C)Copyright 1997, Microsoft Corporation}
          Media {JF Kennedy.wav}
          Metrics {time:ms; duration: 73000;}
          Spec {MSFT:1.0;}
       </SAMIParam>
    </Head>
    
    <Body>
       <SYNC Start=0>
          <P Class=ENUSCC ID=Source>Pres. John F. Kennedy
       <SYNC Start=10>
          <P Class=ENUSCC>Let the word go forth,
             from this time and place to friend and foe
             alike that the torch
    </Body>
    </SAMI>


Credits
=======

Companies
---------

|cirb|_ CIRB / CIBG

* `Contact CIRB <mailto:irisline@irisnet.be>`_

|makinacom|_

* `Planet Makina Corpus <http://www.makina-corpus.org>`_
* `Contact Makina Corpus <mailto:python@makina-corpus.org>`_

Authors

- JeanMichel FRANCOIS aka toutpt <toutpt@gmail.com>

.. Contributors

.. |cirb| image:: http://www.cirb.irisnet.be/logo.jpg
.. _cirb: http://cirb.irisnet.be
.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com
.. _youtube: 