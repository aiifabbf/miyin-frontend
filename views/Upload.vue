<template>
    <!-- <v-layout row justify-center>
    </v-layout> -->
    <v-dialog v-model="active" max-width="600px">
        <template v-slot:activator="{on}">
            <v-btn fab absolute top right dark color="red" @click="active = true">
                <v-icon center>add</v-icon>
            </v-btn>
        </template>

        <v-card>
            <v-card-title>
                <span class="headline">上传视频</span>
            </v-card-title>
            <v-card-text>
                <v-container grid-list-md>
                    <v-layout wrap>
                        <v-flex md12>
                            <input type="file">
                        </v-flex>
                        <v-flex md12>
                            <v-select v-model="categories" :items="allowedCategories" multiple label="选择类别">
                                <template v-slot:selection="{item, index}">
                                    <v-chip>
                                        {{ item }}
                                    </v-chip>
                                </template>
                            </v-select>
                        </v-flex>
                        <v-flex md12>
                            <v-text-field label="标题" v-model="title"></v-text-field>
                        </v-flex>
                        <v-flex md12>
                            <v-textarea label="描述" v-model="description" auto-grow></v-textarea>
                        </v-flex>
                    </v-layout>
                </v-container>
            </v-card-text>
            <v-card-actions>
                <v-btn flat color="red" @click="active = false">取消</v-btn>
                <v-btn flat @click="upload" :disabled="uploading">上传</v-btn>
                <v-progress-circular v-if="uploading" indeterminate></v-progress-circular>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
    export default {
        name: "upload",
        data: function () {
            return {
                active: false,
                categories: [],
                title: "",
                description: "",
                uploading: false,
                allowedCategories: [
                    "音乐",
                    "影视",
                    "动漫",
                    "综艺娱乐",
                    "生活",
                ],
            }
        },
        methods: {
            revert: function () {
                this.categories = [];
                this.title = "";
                this.description = "";
            },
            upload: function () {
                let self = this;
                let form = new FormData();
                let fileInput = document.querySelector("input[type=file]");
                form.append("bytes", fileInput.files[0]);
                // form.append("categories", this.categories);
                // form.append("title", this.title);
                // form.append("description", this.description);
                form.append("meta", JSON.stringify({
                    categories: this.categories,
                    title: this.title,
                    description: this.description
                }));

                let feed = {
                    "title": this.title,
                    "likes": 0,
                    "src": "",
                    "categories": this.categories.concat(["我上传的"])
                };
                let reader = new FileReader();
                reader.addEventListener("load", function(event) {
                    feed.src = event.target.result;
                    self.$emit("upload", feed);
                });
                reader.readAsDataURL(fileInput.files[0]);

                console.log(form);
                this.uploading = true;
                setTimeout(function () {
                    self.uploading = false;
                    self.revert();
                    self.active = false;
                }, 2000);
            }
        }
    }
</script>