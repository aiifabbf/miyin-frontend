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
                uploading: false,
                allowedCategories: [
                    "时下流行",
                    "二极管",
                    "三极管",
                    "真空管",
                    "电容",
                    "电阻",
                ],
            }
        },
        methods: {
            upload: function () {
                let form = new FormData();
                let fileInput = document.querySelector("input[type=file]");
                form.append("bytes", fileInput.files[0]);
                form.append("categories", this.categories);
                console.log(form);
                this.uploading = true;
                let self = this;
                setTimeout(function() {
                    self.uploading = false;
                }, 2000);
            }
        }
    }
</script>