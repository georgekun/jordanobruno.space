<template>
    <div class="project-description">
        
        <div class="head_text">
            <div>
                <h3>{{ typeProject }}</h3>
                <h1>{{ nameProject }}</h1>
            </div>
        </div>

        <!-- <ProjectCard /> -->
        <Cheeps :names="cheeps"></Cheeps>
        <h2>Описание проекта</h2>
        <div class="project_text">
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Beatae officia, libero hic iure voluptatibus facere maiores animi ad error neque nobis asperiores nemo porro rerum aliquam recusandae aliquid sequi voluptate. Temporibus voluptatem culpa, debitis hic nisi error facere ea aliquam, non aspernatur tenetur obcaecati perspiciatis fugiat velit, numquam modi quos facilis qui! Dignissimos, fugit quam? Laborum quibusdam perspiciatis dolorum, aperiam temporibus laudantium deleniti, eum excepturi consequuntur explicabo perferendis ex unde, suscipit doloremque aliquam velit voluptatem. Ea quibusdam perferendis natus et velit odit vitae voluptatem ducimus quo, expedita laboriosam in ut dolorem mollitia eos officiis deserunt dicta explicabo cum facere? Quos!
        </div>
        <h3>Скриншоты</h3>
        <Slider></Slider>

    </div>
</template>

<script>
import ProjectCard from '@/components/ProjectCard.vue';
import Cheeps from '@/components/Cheeps.vue';
import Slider from '@/components/Slider.vue';

export default{
    components:{
        ProjectCard,
        Cheeps,
        Slider
    },
    data(){
        return {
            typeProject:"Веб-сайт",
            nameProject: "Лчиный кабинет для компании забюрист",
            cheeps: ['linux', 'vuejs', 'djangorestframework', 'docker', 'nginx', 'django', 'django', 'django', 'django', 'django'
            , 'django', 'django', 'django', 'django', 'django']
        }
    }
}
</script>

<style scoped>
h3{
    color:var(--main-green);
}

.head_text{
    min-height: 0;
    margin-top:20vh;
}

.project_text{
    max-width:700px;
    width:100%;
    font-size:17px;
    color: #fff;
    letter-spacing: .5px;
    margin:16px auto;
    font-family: Lato, sans-serif;
    font-weight: 300;
    line-height: 24px;
    display: block;
    
}
</style>