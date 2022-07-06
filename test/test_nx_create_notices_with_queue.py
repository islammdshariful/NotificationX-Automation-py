import pytest

from pages.comment_notice import Comment
from pages.contact_form_notice import ContactForm
from pages.custom_notice import Custom
from pages.donation import Donation
from pages.download_stats import DownloadStats
from pages.e_learning_notice import ELearning
from pages.email_subs_notice import EmailSubscription
from pages.inline_notice import Inline
from pages.notification_bar import NotificationBar
from pages.page_analytics import PageAnalytics
from pages.review_notice import Review
from pages.sale_notice import Sale


@pytest.mark.order(1)
def test_comment_notice(browser):
    comment = Comment(browser)
    comment.load()
    comment.create_comment_notice('n', 'y', 'L')  # Advanced Design - Queue Management - Position


@pytest.mark.order(2)
def test_sale_woo_notice(browser):
    sale = Sale(browser)
    sale.load()
    sale.create_sale_notice('woo', 'n', 'y', 'R')  # Source - Advanced Design - Queue Management - Position


@pytest.mark.order(3)
def test_sale_edd_notice(browser):
    sale = Sale(browser)
    sale.load()
    sale.create_sale_notice('edd', 'n', 'y', 'L')  # Source - Advanced Design - Queue Management - Position


@pytest.mark.order(4)
def test_review_org_notice(browser):
    review = Review(browser)
    review.load()
    review.create_review_notice('org-review', 'n', 'y', 'R')  # Source - Advanced Design - Queue Management - Position


@pytest.mark.order(5)
def test_review_woo_notice(browser):
    review = Review(browser)
    review.load()
    review.create_review_notice('woo-review', 'n', 'y', 'L')  # Source - Advanced Design - Queue Management - Position


@pytest.mark.order(6)
def test_d_stats_notice(browser):
    d_stats = DownloadStats(browser)
    d_stats.load()
    d_stats.create_d_stats_notice('n', 'y', 'R')  # Advanced Design - Queue Management - Position


@pytest.mark.order(7)
def test_e_learning_notice(browser):
    e_learning = ELearning(browser)
    e_learning.load()
    e_learning.create_e_learning_notice('tutor', 'n', 'y',
                                        'L')  # Source - Advanced Design - Queue Management - Position


@pytest.mark.order(8)
def test_donation_notice(browser):
    donation = Donation(browser)
    donation.load()
    donation.create_donation_notice('n', 'y', 'R')  # Advanced Design - Queue Management - Position


@pytest.mark.order(9)
def test_nxbar_notice(browser):
    nxbar = NotificationBar(browser)
    nxbar.load()
    nxbar.create_nxbar_notice('nxbar', 'n', 'T')  # Source - Advanced Design -  Position


@pytest.mark.order(10)
def test_nxbar_w_elementor_notice(browser):
    nxbar = NotificationBar(browser)
    nxbar.load()
    nxbar.create_nxbar_notice('nxbarel', 'null', 'B')


@pytest.mark.order(11)
def test_contact_form_notice(browser):
    contact_form = ContactForm(browser)
    contact_form.load()
    contact_form.create_review_notice('cf7', 'n', 'y', 'L')  # Source - Advanced Design - Queue Management - Position


@pytest.mark.order(12)
def test_page_analytics_notice(browser):
    page_analytics = PageAnalytics(browser)
    page_analytics.load()
    page_analytics.create_page_analytics_notice('n', 'y', 'L')  # Advanced Design - Queue Management - Position


@pytest.mark.order(13)
def test_custom_notice(browser):
    custom = Custom(browser)
    custom.load()
    custom.create_custom_notice('n', 'y', 'R')  # Advanced Design - Queue Management - Position


@pytest.mark.order(14)
def test_inline_edd_notice(browser):
    inline = Inline(browser)
    inline.load()
    inline.create_inline_notice('edd', 'count')  # Source - Type


@pytest.mark.order(15)
def test_inline_woo_count_notice(browser):
    inline = Inline(browser)
    inline.load()
    inline.create_inline_notice('woo', 'count')  # Source - Type


@pytest.mark.order(16)
def test_inline_woo_stock_out_notice(browser):
    inline = Inline(browser)
    inline.load()
    inline.create_inline_notice('woo', 'stockout')  # Source - Type


@pytest.mark.order(17)
def test_inline_tutor_count_notice(browser):
    inline = Inline(browser)
    inline.load()
    inline.create_inline_notice('tutor', 'count')  # Source - Type


@pytest.mark.order(18)
def test_email_subscription_notice(browser):
    email_subs = EmailSubscription(browser)
    email_subs.load()
    email_subs.create_email_subs_notice('mc', 'n', 'n', 'R')  # Source - Advanced Design - Queue Management - Position
