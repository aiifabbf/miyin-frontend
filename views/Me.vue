<template>
    <v-container fluid grid-list-lg>
        <v-layout row wrap>
            <v-flex md12>
                <v-card>
                    <v-img :src="profile.avatar"></v-img>
                    <v-chip absolute top left>{{ profile.role }}</v-chip>
                    <v-card-title>
                        <!-- <h1>{{ profile.name }}</h1> -->
                        {{ profile.name }}
                    </v-card-title>
                    <v-card-actions style="position: relative;">
                        <!-- <v-btn flat>
                            我喜欢过的视频
                        </v-btn> -->
                        <upload></upload>
                        <!-- <v-list>
                            <v-list-tile @click="">
                                我喜欢过的视频
                            </v-list-tile>
                            <v-list-tile @click="">
                                <upload></upload>
                            </v-list-tile>
                            <v-list-tile @click="">
                                我上传的视频
                            </v-list-tile>
                        </v-list> -->
                    </v-card-actions>
                </v-card>
            </v-flex>
            <v-flex md12>
                觅音 © 2019
                <p>
                    <a href="about">关于我们</a> ·
                    <a href="career">工作机会</a> ·
                    <a href="cooperate">商务合作</a>
                </p>
            </v-flex>
        </v-layout>
        <!-- <upload :active="uploading"></upload> -->
    </v-container>
</template>

<script>
    import Upload from "./Upload.vue"

    export default {
        name: "me",
        data: function () {
            return {
                // uploading: false
            }
        },
        props: [
            "profile"
        ],
        components: {
            Upload: Upload
        }
    }
</script>