<template>
    <div id="app">
        <link href='https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900|Material+Icons'
            rel="stylesheet">
        <!-- <header>

        </header>
        <main class="container">
            <trends :feeds="feeds" />
            <trends :feeds="feeds"></trends>
            <me :profile="profile"></me>
        </main>
        <footer>

        </footer> -->
        <v-app style="background: url(tomoko-uji-627708-unsplash.jpg) no-repeat; background-attachment: fixed; background-size: cover;">
            <!-- <v-navigation-drawer app></v-navigation-drawer> -->
            <!-- <v-toolbar app></v-toolbar> -->
            <v-content>
                <v-container>
                    <!-- <router-view></router-view> -->
                    <v-layout>
                        <v-flex md2>
                        </v-flex>
                        <v-flex md8>
                            <trends :feeds="filteredFeeds"></trends>
                        </v-flex>
                        <v-flex md2>
                        </v-flex>
                    </v-layout>
                </v-container>
            </v-content>
            <!-- fixed content -->
            <v-content style="width: 100vw; position: fixed; top: 0; pointer-events: none;">
                <v-container>
                    <v-layout>
                        <v-flex md2 style="pointer-events: auto;">
                            <categories :categories.sync="categories" :activeCategory="activeCategory"
                                v-on:update:activeCategory="updateActiveCategory($event)"></categories>
                        </v-flex>
                        <v-flex md8></v-flex>
                        <v-flex md2 style="pointer-events: auto;">
                            <me :profile="profile" v-on:upload="onUpload($event)"></me>
                        </v-flex>
                    </v-layout>
                </v-container>
            </v-content>
            <v-footer></v-footer>
        </v-app>
    </div>
</template>

<!-- <style>
html, body {
    margin: 0;
    padding: 0;
    background: white;
}

html {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

.container {
    max-width: 1200px;
    margin: 5rem auto;
    display: flex;
    justify-content: space-between;
    align-content: flex-start;
}
</style> -->

<style>
    a {
        text-decoration: none;
    }
</style>

<script>
    import Trends from "./views/Trends.vue"
    import Me from "./views/Me.vue"
    import Categories from "./views/Categories.vue"

    import "vuetify/dist/vuetify.min.css"

    export default {
        data: function () {
            return {
                msg: "hi",
                feeds: [
                    {
                        "title": "你从未听过的上海话版“if you”",
                        "likes": 23412,
                        "src": "http://45.62.105.13:8000/1.mp4",
                        "categories": [
                            "时下流行",
                            "音乐"
                        ]
                    },
                    {
                        "title": "中国有嘻哈！燃炸全国具有代表性五种方言混合说唱",
                        "likes": 23412,
                        "src": "http://45.62.105.13:8000/2.mp4",
                        "categories": [
                            "时下流行",
                            "音乐"
                        ]
                    },
                    {
                        "title": "普通话＋陕西西安话＋东北话版《Tell me》",
                        "likes": 23412,
                        "src": "http://45.62.105.13:8000/3.mp4",
                        "categories": [
                            "时下流行",
                            "音乐"
                        ],
                        "requireVIP": true
                    },
                    {
                        "title": "方言版《卡路里》吓坏小姐姐，看看有没有你家乡的方言版卡路里",
                        "likes": 23412,
                        "src": "http://45.62.105.13:8000/4.mp4",
                        "categories": [
                            "时下流行",
                            "音乐"
                        ]
                    },
                    {
                        "title": "论吃货杨紫的自我修养——据小吃辨方言",
                        "likes": 23412,
                        "src": "http://45.62.105.13:8000/5.mp4",
                        "categories": [
                            "时下流行",
                            "影视"
                        ]
                    },
                    {
                        "title": "还珠格格四川版——千万不要裸辞！",
                        "likes": 23412,
                        "src": "http://45.62.105.13:8000/6.mp4",
                        "categories": [
                            "时下流行",
                            "影视"
                        ]
                    },
                    {
                        "title": "你从未看过的长沙话版老九门",
                        "likes": 23412,
                        "src": "http://45.62.105.13:8000/7.mp4",
                        "categories": [
                            "时下流行",
                            "影视"
                        ],
                        "requireVIP": true
                    },
                    {
                        "title": "《武林外传》各方人士尬方言，吕秀才搞笑了，哈哈！",
                        "likes": 23412,
                        "src": "http://45.62.105.13:8000/8.mp4",
                        "categories": [
                            "时下流行",
                            "影视"
                        ]
                    },
                    {
                        "title": "看天津话可以毁几个萌角色",
                        "likes": 23412,
                        "src": "http://45.62.105.13:8000/9.mp4",
                        "categories": [
                            "时下流行",
                            "动漫"
                        ]
                    },
                    {
                        "title": "杰大方言现场版魔道祖师",
                        "likes": 23412,
                        "src": "http://45.62.105.13:8000/10.mp4",
                        "categories": [
                            "时下流行",
                            "动漫"
                        ],
                        "requireVIP": true
                    },
                    {
                        "title": "方言版小猪佩奇",
                        "likes": 23412,
                        "src": "http://45.62.105.13:8000/11.mp4",
                        "categories": [
                            "时下流行",
                            "动漫"
                        ]
                    },
                    {
                        "title": "英雄方言秀 成吨的伤害准备好了么",
                        "likes": 23412,
                        "src": "http://45.62.105.13:8000/12.mp4",
                        "categories": [
                            "时下流行",
                            "动漫"
                        ]
                    },
                    {
                        "title": "撒贝宁方言大合集",
                        "likes": 23412,
                        "src": "http://45.62.105.13:8000/13.mp4",
                        "categories": [
                            "时下流行",
                            "综艺娱乐"
                        ]
                    },
                    {
                        "title": "papi酱 台湾腔酱东北话合辑",
                        "likes": 23412,
                        "src": "http://45.62.105.13:8000/14.mp4",
                        "categories": [
                            "时下流行",
                            "综艺娱乐"
                        ]
                    },
                    {
                        "title": "来听听汪涵用湖南话朗诵的《沁园春·雪》",
                        "likes": 23412,
                        "src": "http://45.62.105.13:8000/15.mp4",
                        "categories": [
                            "时下流行",
                            "综艺娱乐"
                        ]
                    },
                    {
                        "title": "杨洋安徽话送祝福",
                        "likes": 23412,
                        "src": "http://45.62.105.13:8000/16.mp4",
                        "categories": [
                            "时下流行",
                            "综艺娱乐"
                        ]
                    },
                    {
                        "title": "上海话版土味情话",
                        "likes": 23412,
                        "src": "http://45.62.105.13:8000/17.mp4",
                        "categories": [
                            "时下流行",
                            "生活"
                        ],
                        "requireVIP": true
                    },
                    {
                        "title": "各国方言大比拼，遇到中国方言的时候，都弱爆了",
                        "likes": 23412,
                        "src": "http://45.62.105.13:8000/18.mp4",
                        "categories": [
                            "时下流行",
                            "生活"
                        ]
                    },
                    {
                        "title": "经典大连话 倒鸭子 保险理赔",
                        "likes": 23412,
                        "src": "http://45.62.105.13:8000/19.mp4",
                        "categories": [
                            "时下流行",
                            "生活"
                        ]
                    },
                    {
                        "title": "各地方言大比拼",
                        "likes": 23412,
                        "src": "http://45.62.105.13:8000/20.mp4",
                        "categories": [
                            "时下流行",
                            "生活"
                        ]
                    },
                ],
                filteredFeeds: [],
                profile: {
                    name: "Tao Zhengbing",
                    // avatar: "https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1553743816&di=6db28c143d1bec6fec1982453a697970&src=http://pic.downyi.com/upload/2017-7/201776185638086080.jpg"
                    avatar: "../assets/user.svg",
                    role: "普通会员"
                },
                categories: [
                    "时下流行",
                    "音乐",
                    "影视",
                    "动漫",
                    "综艺娱乐",
                    "生活",
                    "我喜欢的",
                    "我上传的",
                    "全部"
                ],
                activeCategory: "时下流行",
            }
        },
        methods: {
            updateActiveCategory: function (activeCategory) {
                let self = this;
                console.log(activeCategory);
                this.activeCategory = activeCategory;
                if (activeCategory === "全部") {
                    this.filteredFeeds = this.feeds;
                } else {
                    this.filteredFeeds = this.feeds.filter(function (v) {
                        if (v.categories.indexOf(activeCategory) !== -1) {
                            return true;
                        } else {
                            return false;
                        }
                    });
                }
                this.feeds.map(function (feed) {
                    if (feed.requireVIP && self.profile.role !== "大会员") {
                        feed.playable = false;
                    } else {
                        feed.playable = true;
                    };
                    console.log(feed);
                });
                window.scrollTo({ top: 0 });
            },
            onUpload: function (event) {
                console.log(event);
                event.requireVIP = false;
                this.feeds.splice(0, 0, event);
                this.updateActiveCategory(this.activeCategory);
            }
        },
        mounted: function () {
            this.updateActiveCategory(this.activeCategory);
        },
        components: {
            Trends: Trends,
            Me: Me,
            Categories: Categories
        }
    }
</script>