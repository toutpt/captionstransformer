try:
    import unittest2 as unittest
except ImportError:
    import unittest
from captionstransformer import youtube


class TestYoutube(unittest.TestCase):

    def test_get_video_id(self):
        classic = youtube.get_video_id("http://www.youtube.com/watch?v=KETCcNzrOb4")
        self.assertEqual(classic, 'KETCcNzrOb4')

        https = youtube.get_video_id("https://www.youtube.com/watch?v=KETCcNzrOb4")
        self.assertEqual(https, 'KETCcNzrOb4')

        notube = youtube.get_video_id("http://www.notube.com/watch?v=KETCcNzrOb4")
        self.assertEqual(notube, None)

        nov = youtube.get_video_id("http://www.youtube.com/watch?s=KETCcNzrOb4")
        self.assertEqual(nov, None)

        vnotfirst = youtube.get_video_id("http://www.youtube.com/watch?s=toto&v=KETCcNzrOb4")
        self.assertEqual(vnotfirst, "KETCcNzrOb4")

    def test_get_captions(self):
        url = "http://www.youtube.com/watch?v=KETCcNzrOb4"
        captions = youtube.get_captions(url, 'fr')
        self.assertEqual(len(captions), 13)


if __name__ == '__main__':
    unittest.main()