"""
As breadcrumb menùs are quite popular today, I won't digress much on explaining
them, leaving the wiki link to do all the dirty work in my place.

What might not be so trivial is instead to get a decent breadcrumb from your
current url. For this kata, your purpose is to create a function that takes a
url, strips the first part (labelling it always HOME) and then builds it making
each element but the last a <a> element linking to the relevant path; last has
to be a <span> element getting the active class.

All elements need to be turned to uppercase and separated by a separator,
given as the second parameter of the function; the last element can terminate
in some common extension like .html, .htm, .php or .asp; if the name of the last
 element is index.something, you treat it as if it wasn't there, sending users
 automatically to the upper level folder.

A few examples can be more helpful than thousands of words of explanation, so
here you have them:

generate_bc("mysite.com/pictures/holidays.html", " : ") ==
    '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> :
     <span class="active">HOLIDAYS</span>'

generate_bc("www.codewars.com/users/GiacomoSorbi", " / ") ==
    '<a href="/">HOME</a> / <a href="/users/">USERS</a> /
     <span class="active">GIACOMOSORBI</span>'
generate_bc("www.microsoft.com/docs/index.htm", " * ") ==
    '<a href="/">HOME</a> * <span class="active">DOCS</span>'
"""
import re

simple_anchor = '<a href="{url}">{name}</a>'
span_anchor = '<span class="active">{name}</span>'
ignored_words = ["the", "of", "in", "from", "by", "with", "and", "or", "for",
                 "to", "at", "a"]
web_page_extensions = [".html", ".htm", ".php", ".asp"]
ignored_words_re = r"(\b(?:the|of|in|from|by|with|and|or|for|to|at|a)-)"
ignored_words_end_re = r"-(the|of|in|from|by|with|and|or|for|to|at|a)$"


def make_name_from_url(string):
    for ext in web_page_extensions:
        if ext in string:
            string = string.replace(ext, '')
    if len(string) <= 30:
        return string.replace('-', ' ').upper()
    else:
        # for word in ignored_words:
        #     string = string.replace('-' + word + '-', '-')
        string = re.sub(ignored_words_re, '', string)
        print(string)
        string = re.sub(ignored_words_end_re, '', string)
        res = "".join([word[0].upper() for word in string.split('-')])
        return res


def generate_bc(url, separator):
    url = url.replace('://', '')
    pages = url.split('#')[0].split('?')[0].split('/')
    if (pages[-1].split('.')[0] == 'index' and
        '.' + pages[-1].split('.')[1] in web_page_extensions) \
            or pages[-1] == "":
        pages.pop()
    res = ""
    pages[0] = ''
    for i, page in enumerate(pages):
        if i == len(pages) - 1:
            page = page if page else 'HOME'
            res += span_anchor.format(name=make_name_from_url(page))
        elif page == '':
            res += simple_anchor.format(name='HOME', url='/') + f"{separator}"
        else:
            res += simple_anchor.format(name=make_name_from_url(page), url='/'. \
                                        join(
                pages[:i + 1]) + '/') + f"{separator}"
    return res


if __name__ == "__main__":
    print(generate_bc(
        "codewars.com/immunity-uber-for-the-research-the-from-of-transmutation/app/eurasian-research-from-bioengineering-pippi-kamehameha/secret-page.php#conclusion",
        " >>> "))
    assert generate_bc("mysite.com/pictures/holidays.html", " : ") == \
           '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>'
    print(generate_bc("www.codewars.com/users/GiacomoSorbi?ref=CodeWars",
                      " / "))
    assert generate_bc("www.codewars.com/users/GiacomoSorbi?ref=CodeWars",
                       " / ") == \
           '<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">GIACOMOSORBI</span>'
    print(generate_bc(
        "www.microsoft.com/important/confidential/docs/index.htm#top", " * "))
    assert generate_bc(
        "www.microsoft.com/important/confidential/docs/index.htm#top", " * ") \
           == '<a href="/">HOME</a> * <a href="/important/">IMPORTANT</a> * <a href="/important/confidential/">CONFIDENTIAL</a> * <span class="active">DOCS</span>'
    print(generate_bc(
        "mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.asp",
        " > "))
    assert generate_bc(
        "mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.asp",
        " > ") \
           == '<a href="/">HOME</a> > <a href="/very-long-url-to-make-a-silly-yet-meaningful-example/">VLUMSYME</a> > <span class="active">EXAMPLE</span>'
    assert generate_bc(
        "www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi",
        " + ") \
           == '<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO SORBI</span>'
