<template>
    <div class="home">
        
        <HeadText></HeadText>

        <div class="btn-group">
            <MainButton @click="scrollToBottom" class="btn-item">Нанять</MainButton>
            <MainButton @click="downloadResume" class="btn-item">Резюме</MainButton>
        </div>

        <SocialMedia></SocialMedia>

        <h2>Что я предлагаю</h2>
        <HomeCardBoard />

        <h2>Изучите недавние работы</h2>
        <ProjectsBoard :latest="true"/>
        <h2>Или напишите сейчас</h2>
        <Form />

    </div>
</template>

<script>
import ProjectsBoard from "@/layouts/ProjectsBoard.vue"
import MainButton from "@/components/MainButton.vue";
import Form from "@/components/Form.vue";
import HeadText from "@/components/HeadText.vue";
import SocialMedia from '@/components/SocialMedia.vue';
import HomeCardBoard from "@/layouts/HomeCardBoard.vue";


import axios from "axios"
import { BASE_URL } from "@/config";
import { mapGetters } from "vuex"
import { download } from '@/utils'

export default{
    data(){
        return {
        }
    },
    components:{
        ProjectsBoard,
        MainButton,
        Form,
        MainButton,
        SocialMedia,
        HeadText,
        HomeCardBoard
    },
    compuded:{
        ...mapGetters('main', ['getInfoProfile'])
    },
    methods:{
       scrollToBottom(){
        window.scrollTo({
                top:document.documentElement.scrollHeight,
                behavior: 'smooth'
            });
       },
        downloadResume(){
            const url = BASE_URL + "personal/resume-pdf/"
            download(url)
        },
     
    },
    mounted(){
        
    }
}
</script>

<style scoped>
.btn-group{
    margin-top:30px;
    
}
.btn-item{
    margin-bottom:10px;
    margin-right:10px;
}
h2{
    color:white;
}
.home{
    margin:20px auto;
}

.head{
    width: 100%;
    display: flex;
    justify-content: left;
    grid-gap:60px;
    flex-wrap: wrap;
    margin:70px 0;
}

@media screen  and (max-width: 800px){
    .head{
        justify-content: center;
    }
}

</style>
