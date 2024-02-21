<template>
    <div class="about">
        <div class="left_bar">
            <Avatar/>
            <h2>Hard skills</h2>
            <SkillLine :percent="90" label="Навык"/>
            <h2>Soft skills</h2>        
            <MainButton text="Скачать резюме"/>  
        </div>

        <div class="right_bar">
            <h1>Князян Джордж Арменович</h1>    
            <h3>Возраст: 22 г., Гражданство: РФ,<br>
                Обазование: Оконченное высшее (бакалавариат)
            </h3>
            <div class="markdown_text">
                {{ md_text }}
            </div>
            <RouterLink to="/contacts" class="contactme">Написать <i></i></RouterLink> 
        </div>
    </div>
</template>

<script>
import { RouterLink } from 'vue-router';
import Avatar from '@/components/Avatar.vue';
import SkillLine from '@/components/SkillLine.vue';
import MainButton from '@/components/MainButton.vue';

export default{
    data(){
        return{
            md_text:''
        }
    },
    components:{
        SkillLine,
        Avatar,
        MainButton
    },
    methods:{
        GET_MD_RESUME_FROM_API(){

        }
    }
}
</script>

<style scoped>
.about{
    display: flex;
    margin:50px 0;
    justify-content: space-between;
    grid-gap:100px;
    flex-wrap: wrap;
}
.left_bar, .right_bar{
    flex-grow:1;
}
.left_bar{
    flex-basis: 25%;
    flex-grow: 30;
    max-width: 300px;
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