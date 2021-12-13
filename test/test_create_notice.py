from pages.comment_notice import Comment


def test_comment_notice(browser):
    comment = Comment(browser)
    comment.load()
    comment.create_comment_notice('L') # L for Left & R for Right

# def test_sale_notice(browser):
