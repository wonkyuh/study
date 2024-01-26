<script>
    import { link } from 'svelte-spa-router'
    import { page, access_token, username, is_login } from '../lib/store'
</script>

<!-- 네비게이션바 -->
<nav class="navbar navbar-expand-lg navbar-dark bg-primary border-bottom">
    <div class="container-fluid">
        <a use:link class="navbar-brand" href="/" on:click="{()=>{$page = 0 }}" style="color: white"><strong>Pybo</strong></a>
        <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation">
            <span class="navbar-toggler-icon" />
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                {#if $is_login }
                    <li class="nav-item">
                        <a use:link href="/user-login" class="nav-link" style="color: white" on:click={() => {
                            $access_token = ''
                            $username = ''
                            $is_login = false
                        }}><strong>로그아웃</strong></a>
                    </li>
                {:else}
                    <li class="nav-item">
                        <a use:link class="nav-link" href="/user-create" style="color: white"><strong>회원가입</strong></a>
                    </li>
                    <li class="nav-item">
                        <a use:link class="nav-link" href="/user-login" style="color: white"><strong>로그인</strong></a>
                    </li>
                {/if}
            </ul>
            {#if $is_login }
            <span class="navbar-text">
                <strong style="color: white">{$username}님 안녕하세요!</strong>
            </span>
            {/if}
        </div>
    </div>
</nav>