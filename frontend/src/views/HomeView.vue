<template>
    <div class="home">
        
        <div class="head">
            <HomeAvatar></HomeAvatar>

            <div>
                <div class="head__text">
                  <ul v-for="p in desc" :key="p.id">
                    <p class="title_p">{{ p.title }}</p>
                    <li v-for="(text, i) in p.span" :key="i">
                        <p class="ia">{{text}}</p>
                    </li>
                  </ul>
                </div>
            </div>

        </div>

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
import HomeAvatar from "@/components/HomeAvatar.vue";


export default{
    data(){
        return{
            desc:[
                {title:"Сфера / профиль образования", 
                    span:['IT / Информационная безопаснсть' ]},

                {title:"В настоящее время", 
                    span:['Full stack web-developer',
                         'Django - FastAPI  and  Vue - Nuxt',
                         'предоставляю услуги по разработке веб-приложений',
                        ]},
            ]
        }
    },
    components:{
        ProjectsBoard,
        MainButton,
        Form,
        HomeAvatar
    },
    compuded:{},
    methods:{
       scrollToBottom(){
        window.scrollTo({
                top:document.documentElement.scrollHeight,
                behavior: 'smooth'
            });
       }
    },
    mounted(){}
}
</script>

<style scoped>
h2{
    color:var(--main-green)
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
.head div{
    margin:auto
}
.head__text{
    color:rgba(255, 255, 255, 0.733);
    align-content: center;
    margin:auto;
    font-size: 20px;
    letter-spacing: 1px;
    width: 100%;
    text-align: center;
}
.head__text ul{
    margin-bottom:10px;
}
.title_p{
    font-weight: 600;
    text-align: left;
    margin-bottom: 3px;
}

.ia{
    margin-left: 20px;
    font-style: italic;
    text-align: left;
    
}
.ia:before{
    content: '-';
    margin:0 10px;
}

@media screen  and (max-width: 800px){
    .head{
        justify-content: center;
    }
    .ia{
        margin-left:5px;
    }
    .ia:before{
        margin:0 3px;
    }
}

</style>
