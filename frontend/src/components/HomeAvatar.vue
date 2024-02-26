<template>
    <div class="home-avatar">
        <div class="avatar_img" :style = returnAvatarLink ></div>
        <p class="name">{{ getInfoProfile.name }}, {{ getInfoProfile.age }}</p>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default{
    name:'HomeAavatar',
    computed:{
        ...mapGetters('main', ['getInfoProfile']),
        returnAvatarLink(){
            const link = this.getInfoProfile.avatar
            return {"background-image":`url(${link})`}
        }
    }
}

</script>

<style scoped>
.name{
    color:white;
    font-style: italic;
    text-align: right;
    padding: 2px 10px;
}
.home-avatar{
    width: 300px;
    height: 350px;
}
.avatar_img{
    border:8px solid rgb(87, 86, 86);
    height: 100%;
    width: 100%;
    background-color: grey;
    background-repeat: no-repeat;
    background-size: cover;
}


</style>