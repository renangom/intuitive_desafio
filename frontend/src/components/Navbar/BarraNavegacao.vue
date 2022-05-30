<template>
    <nav>
        <div class="logo">
            <img src="../../../public/logo_ic.png" />
        </div>
    </nav>
</template>

<script>
export default {
    name: 'BarraNavegacao'
}
</script>

<style>
    nav{ 
        width: 100%;
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.1);
        height: 64px;
        background-color: #fff;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    nav .logo{
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
    }
</style>