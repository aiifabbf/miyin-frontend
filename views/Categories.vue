<template>
    <v-container fluid grid-list-lg>
        <div class="logo">
            <img class="logo__image" src="../Noto_Emoji_KitKat_263a.svg" alt=""> 觅音
        </div>
        <v-card>
            <v-list>
                <v-list-tile v-for="category in categories" @click="$emit('update:activeCategory', category)" :disabled="category === activeCategory">{{ category }}</v-list-tile>
            </v-list>
        </v-card>
    </v-container>

    <!-- <v-card>
        <div class="logo">
            <img class="logo__image" src="../Noto_Emoji_KitKat_263a.svg" alt=""> 觅音
        </div>
        <v-navigation-drawer floating permanent value="音乐">
            <v-list>
                <v-list-tile v-for="category in categories" @click="">{{ category }}</v-list-tile>
            </v-list>
        </v-navigation-drawer>
    </v-card> -->
</template>

<style>
    .logo {
        height: 4rem;
        font-size: 2rem;
    }

    .logo__image {
        height: 3rem;
        vertical-align: text-bottom;
    }
</style>

<script>
    export default {
        name: "categories",
        props: ["categories", "activeCategory"]
    }
</script>