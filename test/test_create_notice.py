from pages.comment_notice import Comment
from pages.donation import Donation
from pages.download_stats import DownloadStats
from pages.e_learning_notice import ELearning
from pages.notification_bar import NotificationBar
from pages.review_notice import Review
from pages.sale_notice import Sale


def test_comment_notice(browser):
    comment = Comment(browser)
    comment.load()
    comment.create_comment_notice('L') # L for Left & R for Right


def test_sale_woo_notice(browser):
    sale = Sale(browser)
    sale.load()
    sale.create_sale_notice('woo', 'R')


def test_sale_edd_notice(browser):
    sale = Sale(browser)
    sale.load()
    sale.create_sale_notice('edd', 'L')


def test_review_org_notice(browser):
    review = Review(browser)
    review.load()
    review.create_review_notice('org', 'R')


def test_review_woo_notice(browser):
    review = Review(browser)
    review.load()
    review.create_review_notice('woo', 'L')


def test_d_stats_notice(browser):
    d_stats = DownloadStats(browser)
    d_stats.load()
    d_stats.create_d_stats_notice('R')


def test_e_learning_notice(browser):
    e_learning = ELearning(browser)
    e_learning.load()
    e_learning.create_e_learning_notice('tutor', 'L')


def test_donation_notice(browser):
    donation = Donation(browser)
    donation.load()
    donation.create_donation_notice('R')


def test_nxbar_notice(browser):
    nxbar = NotificationBar(browser)
    nxbar.load()
    nxbar.create_nxbar_notice('nxbar', 'T')


def test_nxbar_w_elementor_notice(browser):
    nxbar = NotificationBar(browser)
    nxbar.load()
    nxbar.create_nxbar_notice('nxbarel', 'T')
