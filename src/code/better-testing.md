Date: 2012-04-12 19:18
Title: Getting Better at Testing
Slug: better-testing

I started with unit testing about 4 years ago. I started writing what were
probably integration tests, when I was working on the database backend of our
application. The tests I wrote were designed to make sure that our process
which saved data actually saved data. Saving data involved creating a document,
calling save on it, which would save it in the file system-based database,
which would hit the file system. Testing it was saved correctly meant calling
open on a document, which hit the database, which hit the file system.

# I'm doing it wrong

A bit later, I came across this quote:

> A test is not a unit test if:

> * It talks to the database
> * It communicates across the network
> * It touches the file system
> * It can't run at the same time as any of your other unit tests
> * You have to do special things to your environment (such as editing config
>   files) to run it.

> &mdash; [Michael Feathers: A Set of Unit Testing Rules][mfeathers]

I hadn't done all those things, but most of my tests did at least 2 of them[^1].

Regardless of the philosophical point of whether what I had written were unit
tests, there was a more fundamental problem: **they were slow**.

In order to set up the tests I had to create a database, and initialise its
schema. Then I had to repeatedly open and close the database, saving documents,
and checking they were saved correctly. At the end of the tests they had to
clear up the database.

# Impatience

> We will encourage you to develop the three great virtues of a programmer:
> laziness, impatience, and hubris.  
> &mdash; [Larry Wall, Programming Perl][three-virtues]

Increasingly I was writing unit tests which I didn't bother to run during
development - they became another item on my check-list of things to do
before checking code in. If they failed, the specific thing I changed which
might have broken them might have been a while ago, making it hard to track
down.

So a while ago I tried a strange experiment. I tried to build an entire
website[^2] without opening a browser. I didn't quite make it (eventually I had
to open a browser to check that it looked reasonable), but I got all the models
and views built by writing tests for them[^3].

Using a [quick trick][tdd-django], my app's test suite runs in 2.1s on my
machine, which meant that it was pretty easy to run tests before each
commit[^4]. Being able to specify [particular tests][django-docs-testing] to
run makes test-driven development a practical possibility.

And each time I start a project this way, with a basic set of tests, I find
that I'm more likely to write tests next time I work on it. The tests I write
help me be confident that any changes I make are good, and confidence helps me
get stuff done, and getting stuff done makes me happy.

[^1]: Since writing those first tests, I've started working on a team which
      works on database technology, so avoiding talking to the database is
      pretty tricky, since if you've not talked to the database, you've not
      tested your code.
[^2]: The website was [Ministry Today][ministrytoday], if you're curious. The
      less kind amongst you might well suggest that it looks like a site which
      was built with design as an afterthought.
[^3]: Most of the tests are part of [django-magazine][django-magazine], and
      you can see them on [GitHub][django-magazine-tests].
[^4]: I really ought to play around with [pre-commit hooks][django-git-hooks]
      for this stuff some day.

[mfeathers]: http://www.artima.com/weblogs/viewpost.jsp?thread=126923 "Read Michael Feathers' Unit Testing Rules"
[three-virtues]: http://en.wikipedia.org/wiki/Larry_Wall "The quote is from Programming Perl, by Larry Wall - go take a look at his Wikipedia profile"
[ministrytoday]: http://ministrytoday.org.uk "Visit the Ministry Today site, a journal for Christian leaders"
[django-magazine]: https://github.com/dominicrodger/django-magazine "Take a look at django-magazine, the main open source app behind Ministry Today"
[django-magazine-tests]: https://github.com/dominicrodger/django-magazine/tree/master/magazine/tests "Browse the code for the tests of django-magazine"
[tdd-django]: http://www.dominicrodger.com/tdd-django-south.html "Read about a quick trick for making test runs in Django faster"
[django-git-hooks]: http://tech.yipit.com/2011/11/16/183772396/ "Read about Django pre-commit hooks at the Yipit Django Blog."
[django-docs-testing]: https://docs.djangoproject.com/en/dev/topics/testing/#running-tests "Django Documentation for running just a subset of your unit tests"
