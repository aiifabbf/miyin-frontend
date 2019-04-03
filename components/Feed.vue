<template>
    <!-- <div class="trends__feed">
        <video :src="feed.src" controls></video>
    </div> -->
    <v-card>
        <!-- <v-layout>
            <v-flex grow>
                <video :src="feed.src" controls></video>
            </v-flex>
            <v-flex shrink>
                <v-layout column>
                    <v-btn icon>
                        <v-icon>favorite</v-icon>
                    </v-btn>
                </v-layout>
            </v-flex>
        </v-layout> -->
        <v-img>
            <video :src="feed.src" controls></video>
        </v-img>

        <!-- <v-card-title>
            <div>
                <h3 class="headline">{{ feed.title }}</h3>
                <div>
                    {{ feed.description }}
                </div>
            </div>
            <v-spacer></v-spacer>
            <div>
                <v-btn icon flat color="red">
                    <v-icon>favorite</v-icon>
                </v-btn>
                {{ feed.likes }}
                <v-btn icon>
                    <v-icon>share</v-icon>
                </v-btn>
            </div>
        </v-card-title> -->

        <v-card-title>
            <div>
                <h3 class="headline">
                    {{ feed.title }}
                    <v-chip v-for="category in feed.categories">{{ category }}</v-chip>
                </h3>
                <div>
                    {{ feed.description }}
                </div>
            </div>
            <!-- <v-spacer></v-spacer> -->
        </v-card-title>
        <v-card-actions>
            <!-- <label style="cursor: pointer;">
                <v-btn icon flat color="red" v-if="feed.categories.indexOf('我喜欢的') !== -1" @click="unlike(feed)">
                    <v-icon>favorite</v-icon>
                </v-btn>
                <v-btn icon flat color="red" v-else @click="like(feed)">
                    <v-icon>favorite_border</v-icon>
                </v-btn>
                {{ feed.likes }}
            </label> -->
            <v-btn icon flat color="red" v-if="feed.categories.indexOf('我喜欢的') !== -1" @click="unlike(feed)">
                <v-icon>favorite</v-icon>
            </v-btn>
            <v-btn icon flat color="red" v-else @click="like(feed)">
                <v-icon>favorite_border</v-icon>
            </v-btn>
            {{ feed.likes }}
            <v-btn icon>
                <v-icon>share</v-icon>
            </v-btn>
        </v-card-actions>
        <div>
        </div>
    </v-card>
</template>

<style>
    video {
        width: 100%;
    }
</style>

<script>
    export default {
        name: "feed",
        props: [
            "feed"
        ],
        methods: {
            like: function (feed) {
                console.log(feed);
                feed.categories.push("我喜欢的");
                feed.likes += 1;
            },
            unlike: function (feed) {
                console.log(feed);
                let likeIndex = feed.categories.indexOf("我喜欢的");
                feed.categories = feed.categories.slice(0, likeIndex).concat(feed.categories.slice(likeIndex + 1));
                feed.likes -= 1;
            }
        }
    }
</script>