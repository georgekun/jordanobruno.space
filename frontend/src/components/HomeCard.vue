<template>
    <div class="card">
        <div class="card-body">
            <i :class="icon"></i>
            <h5>{{title}}</h5>
            <p>{{ text }}</p>
        </div> 
    </div>
</template>

<script>

export default{
    name:'HomeCard',
    props:{
        icon:String,
        title:String,
        text:String
    },
    computed:{

    }
}

</script>

<style scoped>
    .card{
        max-width:320px;
        border-radius:0.25rem;
        box-shadow: 2px 3px 10px rgba(206, 212, 218, 0.3);
        border: 1px solid #dee2e6 !important;
        text-align: center;
    }
    .card-body{
        padding:55px 0 40px;
    }

    .card-body i {
        display: block;
        font-size: 40px;
      
        color: var(--main-green);
        margin:0 auto;
        margin-bottom: 18px;
    }
    h5{
        margin-bottom:5px;
        font-size:1.25rem;
    }
    p{
        margin:0.5rem;
        margin-top:1rem;
        font-size: calc(14px +(16 - 14)*((100vw - 320px) /(1200 - 320)));
        margin-bottom: 12px;
        letter-spacing: .6px;
        text-align: center;
        color:rgba(230, 230, 230, 0.824);
    }

    @media screen and (max-width:600px) {
        .card-body{
            padding:10px 0;
        }
        .card-body i {
            font-size: 30px;
            margin-bottom: 0px;
        }
    }
</style>