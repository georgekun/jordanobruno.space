<template>
    <div class="skill_line">
        <label for="group" class="line_label">{{ label }}</label>
        <div id="group">
            <div class="line_back" ></div>
            <div class="line_front" :style="{'width': width}"></div>
        </div>
    </div>
</template>

<script>
export default{
    name: "SkillLine",
    props:{
        label: String,
        percent: Number
    },
    computed: {
        width() {
            return `${this.percent}%`;
        }
    }
}
</script>

<style scoped>
.skill_line{
    width: 100%;
}
.skill_line > div{
    min-height: 4px;
    position: relative;
    margin:10px 0;
}
.line_back{
    width:100%;
    height: 4px;
    background-color: var(--main-grey); 
    position: absolute;
    top:0;
    left:0;
    border-radius:3px;
}
.line_front{
    /* width:90%; */
    height: 4px;
    position: absolute;
    background-color: var(--main-green); 
}

.line_label{
    color:white;
}
</style>