from base.base_driver import init_driver
from page.page import Page


class TestShopCart:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_add_shop_cart(self):
        # 首页，如果没有登录就登录
        self.page.home.login_if_not(self.page)
        # 首页 - 分类
        self.page.home.click_category()
        # 分类 - 商品列表
        self.page.category.click_goods_list()
        # 商品列表 - 商品详情
        self.page.goods_list.click_goods()
        # 商品详情 - 加入购物车
        self.page.goods_detail.click_add_shop_cart()
        # 商品详情 - 选择规格
        self.page.goods_detail.click_spec()
