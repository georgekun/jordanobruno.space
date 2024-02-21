<template>
    <div class="avatar">
        <div class="avatar_img" :style = returnAvatarLink ></div>
    </div>
</template> 

<script>
import { mapGetters } from "vuex"

export default{
    name: "Avatar",
    computed:{
        ...mapGetters('main', ['getInfoProfile']),
        returnAvatarLink(){
            const link = this.getInfoProfile.avatar
            return {"background-image":`url(${link})`}
        }
    },
    methods:{
       
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
    background-color: grey;
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center;
}
</style>