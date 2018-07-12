import xml.etree.ElementTree
from unittest import TestCase


class SitemapWebTests(TestCase):
    app = None

    def setUp(self):
        SitemapWebTests.app = self.get_or_create_web_app()

    # noinspection PyMethodMayBeStatic
    def get_or_create_web_app(self):
        if SitemapWebTests.app:
            return SitemapWebTests.app

        from pypi import main
        app = main({})
        # noinspection PyPackageRequirements
        from webtest import TestApp

        return TestApp(app)

    def get_sitemap_text(self):
        # <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        #     <url>
        #         <loc>http://talkpython.fm/episodes/show/37/python-cybersecurity-and-penetration-testing</loc>
        #         <lastmod>2015-12-08</lastmod>
        #         <changefreq>weekly</changefreq>
        #         <priority>1.0</priority>
        #     </url>
        #     <url>
        #         ...
        #     </url>
        res = self.app.get("/sitemap.xml")
        text = res.text.replace('xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"', '')
        return text

    def test_site_mapped_urls(self):
        text = self.get_sitemap_text()
        x = xml.etree.ElementTree.fromstring(text)
        urls = [
            href.text.strip().replace('http://localhost:6552', '')
            for href in list(x.findall('url/loc'))
        ]
        print('Testing {} urls from sitemap...'.format(len(urls)), flush=True)

        has_tested_projects = False
        for url in urls:
            if '/project/' in url and has_tested_projects:
                continue

            if '/project/' in url:
                has_tested_projects = True

            print('Testing url at ' + url)
            self.app.get(url, status=200)
