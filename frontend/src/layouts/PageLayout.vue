<template>
    <div class="page">
        <div class="wrapper">
            <Header/>
            <slot></slot>
            <UpArrow />
            <Footer />
            <Notification />
            
        </div>
    </div>
</template>

<script>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
import UpArrow from '@/components/UpArrow.vue';
import Notification from '@/components/Notification.vue';

import { mapActions } from "vuex"

export default{
    name:"PageLayout",
    components:{
        Header,
        Footer,
        UpArrow,
        Notification,
        Notification
    },
    methods:{
        ...mapActions('main', ['GET_INFO_PROFILE_FROM_API'])
    },
    mounted(){
        this.GET_INFO_PROFILE_FROM_API()
    },
}

</script>

<style scoped>
.page{

    background-image: linear-gradient(rgba(0, 0, 0, .57), #222),
     url("@/assets/background_page.jpeg");
    background-position: 0 0, 38%;
    background-repeat:no-repeat;
   
    height: 540px; 
    background-size: cover;
    padding:30px 15%;
    position: relative; 
   
}   
.wrapper{
    max-width: 1200px;
}
@media screen and (max-width:1050px){
    .page{
        padding:30px 5%;
        position: relative;
    }   
}
</style>
