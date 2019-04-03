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
        <v-app>
            <!-- <v-navigation-drawer app></v-navigation-drawer> -->
            <!-- <v-toolbar app></v-toolbar> -->
            <v-content>
                <v-container>
                    <!-- <router-view></router-view> -->
                    <v-layout>
                        <v-flex md3>
                            <categories :categories.sync="categories" :activeCategory="activeCategory"
                                v-on:update:activeCategory="updateActiveCategory($event)"></categories>
                        </v-flex>
                        <v-flex md6>
                            <trends :feeds="filteredFeeds"></trends>
                        </v-flex>
                        <v-flex md3>
                            <me :profile="profile"></me>
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
                        src: "http://192.168.73.132/cnks4.imslp.org/files/imglnks/usimg/b/b7/IMSLP305905-PMLP05948-02Epre_cmaj.ogg",
                        likes: 1223,
                        title: "好玩的视频",
                        description: "这个超级好玩的，你看鸟瞰鸟瞰年卡，随便看爱爱爱拉阿拉啦。",
                        categories: ["音乐"]
                    },
                    {
                        src: "http://192.168.73.132/cnks4.imslp.org/files/imglnks/usimg/b/b7/IMSLP305905-PMLP05948-02Epre_cmaj.ogg",
                        likes: 1223,
                        title: "好玩的视频",
                        categories: ["时下流行", "音乐"]
                    }
                ],
                filteredFeeds: [],
                profile: {
                    name: "Tao Zhengbing",
                    avatar: "https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1553743816&di=6db28c143d1bec6fec1982453a697970&src=http://pic.downyi.com/upload/2017-7/201776185638086080.jpg"
                },
                categories: [
                    "时下流行",
                    "二极管",
                    "三极管",
                    "真空管",
                    "电容",
                    "电阻",
                    "我喜欢的",
                    "我上传的",
                    "全部"
                ],
                activeCategory: "时下流行",
            }
        },
        methods: {
            updateActiveCategory: function (activeCategory) {
                console.log(activeCategory)
                this.activeCategory = activeCategory
                if (activeCategory === "全部") {
                    this.filteredFeeds = this.feeds
                } else {
                    this.filteredFeeds = this.feeds.filter(function (v) {
                        if (v.categories.indexOf(activeCategory) !== -1) {
                            return true
                        } else {
                            return false
                        }
                    })
                }
            }
        },
        mounted: function() {
            this.updateActiveCategory(this.activeCategory);
        },
        components: {
            Trends: Trends,
            Me: Me,
            Categories: Categories
        }
    }
</script>