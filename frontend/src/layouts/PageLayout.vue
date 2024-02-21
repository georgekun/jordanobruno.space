<template>
    <div class="page">
        <Header/>
        <slot></slot>
        <UpArrow />
        <Footer />
    </div>
</template>

<script>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
import UpArrow from '@/components/UpArrow.vue';

export default{
    name:"PageLayout",
    components:{
        Header,
        Footer,
        UpArrow
    }
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

@media screen and (max-width:1050px){
    .page{
        padding:30px 5%;
        position: relative;
    }   
}
</style>
