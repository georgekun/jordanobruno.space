<template>
    <div class="header">
        <div>
            <img src="" alt="" class="logo">
            <NavBar/>
        </div>
    </div>
</template>

<script>
import NavBar from './NavBar.vue';
export default{
    name: "Header",
    components:{
        NavBar
    }
}

</script>

<style scoped>
.header > div{
    display: flex;
    justify-content: space-between;
}
</style>
