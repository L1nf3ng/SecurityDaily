from crawler.models import Executor


async def unit_task(url):
    cl = Executor(url)
    # phase 1, request the blog
    blog = await cl.get_blog()
    if blog is None:
        print('the target {} currently not visited!'.format(url))
    print("---------- the posts from {} -----------".format(url.upper()))
    # phase2, analyse the response
    cl.parse_blog(blog)
    # to_show = {'Origin': url.url, 'Articles': cl.posts, 'Len': len(cl.posts)}
    # temp.append(to_show)