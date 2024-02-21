<template>
    <div class="slider">
        <v-carousel
            height="500px"
            :hide-delimiter-background="true"
            show-arrows="hover"
        
            theme="dark"
        >
        <v-carousel-item
            v-for="(slide, i) in getSlides"
            :key="i"
        >
            <v-sheet
            height="100%"
            width="100%"
            >
            <div class="d-flex fill-height justify-center align-center">
                    <v-img
                        width="680px"
                        :aspect-ratio="1"
                        :src="slide.image"
                        cover  
                    ></v-img>
            </div>
            </v-sheet>
        </v-carousel-item>
        </v-carousel>
    </div>
</template>

<script>
import png from "@/assets/main_cat.png"

export default {
    name:"Slider",
    props:{
        slides:Array[Object]
    },
    computed:{
        getSlides(){
            return [...this.firstSlide,...this.slides]
        }
    },
    data(){
        return {
            firstSlide:[
                {image:png}
            ],
        }
    },
}
</script>


<style scoped>
h3{
    color:var(--main-green);
}
.slider{
    margin:30px auto 30px;
    border-radius:10px;
}
</style>