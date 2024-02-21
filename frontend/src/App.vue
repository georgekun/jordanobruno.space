<template>
    <PageLayout>
        <RouterView />
    </PageLayout>
</template>

<script>
import { RouterView } from 'vue-router'
import PageLayout from "@/layouts/PageLayout.vue"

export default{
    components:{
        PageLayout
    }
}
</script>
<style scoped>
</style>
