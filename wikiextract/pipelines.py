# vim: set fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4 softtabstop=4 :
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import os
import sys
import shutil
from lxml import html as lhtml
from lxml import etree
#from xml.dom import minidom
from urlparse import urlparse

class WikiextractPipeline(object):
    def __init__(self):
        self.template = open('wikiextract/docs.html.tpl').read().encode('UTF-8')

    def restructureHtml(self, content):
        '''Add some tags needed to keep style the same as the rest of the site.'''
        # tdom = minidom.parseString(content)
        tdom = lhtml.document_fromstring(content)
        current_id = ''
        inner = []
        deepinner = []
        innerformat = '''\
<div class="section" id="section-{0}">
    <div class="element noborder">
        {1}
    </div>
</div>
'''
        nodes = None

        rootNodes = tdom.getchildren()
        nodes = rootNodes[0].getchildren()[0].getchildren()

        if not nodes:
            # TODO: What is the situation like here?
            nodes = rootNodes[0].getchildren()

        for node in nodes:
            # Element: If it's a heading element, I'll add a special label to be
            # displayed on the right, otherwise just append to the page.
            if node.tag[0] == 'h':
                if current_id:
                    inner.append(innerformat\
                            .format(current_id, ''.join(deepinner))
                            .replace('\\n', '\n').replace("\\'", "'"))
                    
                deepinner = []
                current_id = node.get('id')
                deepinner.append(u'''\
<div class="sideinfo">
    <div class="date normal" id="mark-{0}">{1}</div>
</div>
<{2} class="smalltitle">{1}</{2}>
'''.format(current_id, node.text, node.tag))
            else:
                content = etree.tostring(node, pretty_print=True).replace('\\n', '\n').replace("\\'", "'")
                deepinner.append(content)
        
        # Let's not forget the last lines...
        if deepinner:
            inner.append(innerformat.format(current_id, ''.join(deepinner)))

        return '\n'.join(inner)

    def process_item(self, item, spider):
        item['content'] = self.restructureHtml(item['content'].encode('UTF-8'))
        item['content'] = self.template % item['content']

        url = urlparse(item['url'])
        url = url.path.split('/')[4:]

        # Skip last split in case the URL ends in '/' (paranoia)
        if len(url) >= 1:
            if url[-1] == '':
                url.pop()
            if url[0] == '':
                url = url[1:]

        # Root directory for the extracted pages. 
        root_directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Pages')

        if not os.path.exists(root_directory):
            os.mkdir(root_directory)

        # Directory name for target.
        directory = os.path.join(root_directory, *url[:-1])
        # Directory name of index pages.
        cleandir = os.path.join(root_directory, *url)
        name = url[-1] + '.html'

        # Parent directory not existing?
        needdir = False
        # Make two copies for this file. See comment below.
        copyfile = False

        # We need to make a directory for this file.
        if not os.path.exists(directory):
            needdir = True

        # Turns out that a page has subpages. Move it, create a directory,
        # and move the page into the directory.
        existingname = os.path.join(directory, name)
        if os.path.isfile(existingname):
            # No need to copy, we'll do it here (we're working on a different
            # page now.
            copyfile = False
            # Make a directory for the subpages.
            if not os.path.exists(cleandir):
                os.mkdir(cleandir)
            # Copy. See comment below on .htaccess.
            shutil.copy(existingname, '{0}/index.html'.format(cleandir))
            # Directory existing, we're sure.
            needdir = False
        elif os.path.isdir(cleandir):
            # Exist already as a directory. We'll write the file twice (see below).
            existingname = '{0}/index.html'.format(cleandir)
            needdir = False
            copyfile = True

        # The directory we need doesn't exits yet.
        if needdir:
            os.mkdir(directory)

        # Write the HTML file.
        output = file(existingname, 'w')
    
        with output:
            output.write(item['content'])
            output.close()
   
        # Simplify my relationship with .htaccess. For a directory named Dir we'll have
        # both Dir.html and Dir/index.html (to use MultiViews and live happily).
        if copyfile:
            shutil.copy(existingname, os.path.join(directory, name))

        return item
