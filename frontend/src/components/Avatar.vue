<template>
    <div class="avatar">
        <div class="avatar_img"></div>
    </div>
</template>

<script>
export default{
    name: "Avatar",
    methods:{
        GET_AVATAR_FROM_API(){

        }
    }
}
</script>

<style scoped>
.avatar{
    width:155px;
    height: 150px;
    margin:auto;
}

.avatar_img{
    border-radius: 100%;
    border:2px solid white;
    height: 100%;
    width: 100%;
    background: url('@/assets/background_page.jpeg');
    background-repeat: no-repeat;
    background-size: cover;
}
</style>