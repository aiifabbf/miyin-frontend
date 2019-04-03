<template>
    <!-- <div class="trends">
        <div v-for="feed in feeds">
            <feed :feed="feed"></feed>
        </div>
    </div> -->
    <v-container fluid grid-list-lg>
        <v-layout row wrap>
            <v-flex md12 v-for="feed in feeds">
                <feed :feed="feed"></feed>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<!-- <style>
.trends {
    width: 60%;
    border: 1px solid black;
}
</style> -->

<script>
import Feed from "../components/Feed.vue"

export default {
    name: "trends",
    // data: function() {

    // },
    props: [
        "feeds"
    ],
    components: {
        Feed: Feed
    }
}
</script>