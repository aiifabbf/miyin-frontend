<template>
    <v-dialog v-model="active" max-width="400px">
        <template v-slot:activator="{on}">
            <v-btn color="red" flat @click="active = true">
                开通大会员
            </v-btn>
        </template>

        <v-card>
            <v-card-title>
                <span class="headline">
                    开通“觅音”网站VIP会员免费看
                </span>
            </v-card-title>
            <v-card-text>
                <p>
                    新用户注册VIP首月5元
                </p>
                <p>
                    非会员原价0.5元购买本视频
                </p>
            </v-card-text>
            <v-card-actions>
                <v-btn flat color="red" @click="active = false">开通会员</v-btn>
                <v-btn flat>购买视频</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
    export default {
        name: "vip",
        data: function () {
            return {
                active: false
            }
        }
    }
</script>