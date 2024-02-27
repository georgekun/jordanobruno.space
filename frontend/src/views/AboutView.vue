<template>
    <div class="about">

        <div class="left_bar">
            <Avatar/>
            <h2>{{ getInfoProfile.name }}</h2>
            <h4>Hard skills</h4>

            <SkillLine  v-for="(skill, i) in hard"
                :key = i
                :label="skill.title"
                :percent="skill.percent"
            />

            <h4>Soft skills</h4>      

            <SkillLine  v-for="(skill, i) in soft"
                :key = i
                :label="skill.title"
                :percent="skill.percent"
            />  

            <br>
            <MainButton @click="downloadResume" class="btn" text="">Резюме</MainButton>
        </div>

        <div class="right_bar">
            <div v-html="resume.resume_html"></div>
            <RouterLink to="/contacts" class="contactme">Написать <i></i></RouterLink> 
        </div>

    </div>
</template>

<script>
import axios from "axios"
import { BASE_URL } from "@/config";
import { mapGetters } from "vuex"
import { download } from '@/utils'

import { RouterLink } from 'vue-router';
import Avatar from '@/components/Avatar.vue';
import SkillLine from '@/components/SkillLine.vue';
import MainButton from '@/components/MainButton.vue';

export default{
    data(){
        return{
            resume:{},
            hard:[
                {title:"Python / Django / DRF", percent:90},
                {title:"JS / VueJS 3 / Vuetify", percent:80},
                {title:"Asyncio / Aiohttp", percent:85},
                {title:"Linux", percent:60},
                {title:"Docker", percent:80},
                {title:"Flask / FastAPI", percent:70},
                {title:"SQL / postgresql", percent:60},
                {title:"Scraping", percent:80},
            ],
            soft:[
                {title:"Обучаемость", percent:100},
                {title:"Коммуникабельность", percent:100},
            ]
        }
    },
    components:{
        SkillLine,
        Avatar,
        MainButton
    },
    computed:{
        ...mapGetters('main', ['getInfoProfile'])
    },
    methods:{
        downloadResume(){
            const url = BASE_URL + "personal/resume-pdf/"
            download(url)
        },

        GET_HTML_RESUME_FROM_API(){
            const url = BASE_URL + "personal/resume/"
            axios.get(url)
                .then( r => this.resume = r.data)
                .catch( e => console.log(e) )
        }
    },
    mounted(){
        this.GET_HTML_RESUME_FROM_API()
    }
}
</script>

<style scoped>
.btn{
    border-color:transparent;
    letter-spacing: 2px;
    padding: 5px 10px;
}
.btn:hover{
    color:white;
    border-color:transparent;
}
.btn:after{
    content: "\f019";
    margin-left:12px;
    font-family: fa;
    font-style: normal;
}
.about{
    display: flex;
    margin:50px 0;
    justify-content: space-between;
    grid-gap:100px;
    flex-wrap: wrap;
}
.left_bar, .right_bar{
    flex-grow:1;
    margin:auto
}
.left_bar{
    flex-basis: 25%;
    flex-grow: 30;
    max-width: 300px;
    text-align: center;
}
.right_bar{
    margin-top:20px;
    text-align: center;
    flex-basis: 60%;
    color:#bdbdbd;
}

.right_bar__text{
    
    text-align: center;
    font-size:17px;
    margin-bottom:50px;
}

.contactme{
    color:white;
    margin:5px;
    float:right;
    border-bottom:1px solid white;
}
.contactme:hover{
    color:var(--main-green);
    border-color:var(--main-green);
    transition: 0.4s;
}
.contactme i:after{
    content:"\f061";
    font-style: normal;
    font-family: fa;
}
</style>