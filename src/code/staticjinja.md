Date: 2014-06-14 21:52
Title: Prototyping with staticjinja
Slug: staticjinja

I've started building a website for a friend of mine, who works for
an organisation called [Talitha][talitha].

I wanted to get something up and running quickly (since I figured *a*
website was better than no website), so I just started playing with
[Bootstrap][bootstrap]. From there, I had an idea of what I wanted
the site to look like, and all was well. I threw up a single page
site that introduced the organisation a little bit.

Problem is, then I had to make a second page.

I didn't want to repeat myself (because I'm obsessive like that), and
I didn't feel like setting something up with [Pelican][pelican].

I really just wanted to use Jinja, and extend a base template
somewhere. I started looking for a library that would let me do that,
and came across [staticjinja][staticjinja].

It didn't quite do what I wanted, so I wrote
[a few patches][staticjinja-commits] for it:

1. Added support for static files (which now get copied from a source
   directory to an output directory).
2. Added a standalone build script (called `staticjinja`) to avoid
   needing any custom Python script to build my site.

All this (which took about a week of train journeys...) meant I could
write that [second page][talitha-github], without ever repeating
myself.

It took a lot longer than just copying and pasting that first page,
but I've never been one to shy away from [yak shaving][yak-shaving].

[talitha]: http://www.talitha.org.uk "Take a look at the beginnings of Talitha's website."
[bootstrap]: http://www.getbootstrap.com "Built websites with Bootstrap."
[pelican]: http://www.getpelican.com "Pelican is a static site generator built with Python, and runs this site."
[staticjinja]: http://staticjinja.readthedocs.org/en/latest/ "See staticjinja's documentation."
[staticjinja-commits]: https://github.com/Ceasar/staticjinja/commits?author=dominicrodger "Take a look at my commits to staticjinja."
[talitha-github]: https://github.com/dominicrodger/talitha.org.uk "Take a look at talitha.org.uk's code on GitHub."
[yak-shaving]: http://www.hanselman.com/blog/YakShavingDefinedIllGetThatDoneAsSoonAsIShaveThisYak.aspx "Read Scott Hanselman's definition of Yak Shaving."
