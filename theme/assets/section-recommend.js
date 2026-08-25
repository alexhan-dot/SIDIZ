document.addEventListener("DOMContentLoaded",async()=>{try{await allRecommendProductDataLoaded}catch(error){console.error("Error loading data:",error)}getRecommendProducts()});async function getRecommendProducts(){let swiper_el=null,desc_el=null;const recently_viewed=JSON.parse(localStorage.getItem("recentlyViewed"));let result_products=[];if(recently_viewed&&await fetch("https://sidiz-shopify.sidiz.com/product-metafields",{method:"POST",headers:{Accept:"application/json","Content-Type":"application/json"},body:JSON.stringify({prodHandle:recently_viewed.handle})}).then(response=>response.json()).then(data=>{data.metafields.length>0&&data.metafields.slice(0,4).forEach(metafield=>{result_products.push(metafield)}),result_products.push(recently_viewed.id)}),result_products.length>1){document.querySelector("#recently-viewed").textContent=recently_viewed.name;let recommend_swiper=document.querySelector(".swiper.recommend-swiper"),slides_html="";result_products.forEach((id,index)=>{const product=findProductById(id);if(!product)return;let is_recently=index===result_products.length-1,product_url=product.url,product_image=product.variants[0].featured_image,product_title=product.title,variantData=product.variants[0];for(let i=0;i<product.variants.length;i++)if(product.variants[i].price===product.price_min){variantData=product.variants[i];break}let price_varies=product.price_varies,price=variantData.price,specialPrice=variantData.special_price,eventStartDate=variantData.event_start_dt,eventEndDate=variantData.event_end_dt,customerDiscountRate=0,isEvent=!1,priceTag="";if(eventStartDate&&eventEndDate){const now=new Date,start=new Date(eventStartDate),end=new Date(eventEndDate);now>=start&&now<=end&&(isEvent=!0)}if(isEvent){let priceNum=parseFloat(price.replace(/,/g,"")),specialPriceNum=parseFloat(specialPrice.replace(/,/g,""));priceNum>specialPriceNum&&(customerDiscountRate=Math.round((priceNum-specialPriceNum)/priceNum*100),customerDiscountRate=parseInt(customerDiscountRate,10),priceTag=`
                        <div class="title--discount">\uD68C\uC6D0 \uD560\uC778\uAC00</div>
                        <div class="price--compare">
                            <span class="percent--discount">${customerDiscountRate}%</span>
                            <span class="price--discount">${specialPriceNum.toLocaleString()}\uC6D0${price_varies=="true"?"~":""}</span>
                            <span class="price--original pc">${priceNum.toLocaleString()}\uC6D0${price_varies=="true"?"~":""}</span>
                        </div>
                        <div class="price--original mobile">${priceNum.toLocaleString()}\uC6D0${price_varies=="true"?"~":""}</div>
                    `)}else priceTag=`
                    <div class="price--compare">
                        <span class="price--discount">${Number(price).toLocaleString()}\uC6D0${price_varies=="true"?"~":""}</span>
                    </div>
                `;slides_html+=`
                <div id="product-item-${product.id}" class="product-item swiper-slide">
                    <div class="product-item--image">
                        <img src="${product_image}" alt="${product_title}">
                        <a href="${product_url}"></a>
                        ${is_recently?'<div class="badge-recently">\uCD5C\uADFC \uBCF8 \uC81C\uD488</div>':""}
                    </div>
                    <div class="product-item--text">
                        <div class="product-item--title">${product_title}</div>
                        <div class="product-item--price">
                            ${priceTag}
                        </div>
                    </div>
                </div>
            `}),recommend_swiper.querySelector(".swiper-wrapper").insertAdjacentHTML("afterbegin",slides_html),swiper_el=recommend_swiper,desc_el=document.querySelector(".description.recently")}else swiper_el=document.querySelector(".swiper.recommend-default-swiper"),desc_el=document.querySelector(".description.no-recently");swiper_el.classList.remove("hidden"),desc_el.classList.remove("hidden"),setRecommendSwiper(swiper_el),addSelectItemEvent()}function setRecommendSwiper(swiper_el){new Swiper(swiper_el,{spaceBetween:12,breakpoints:{1024:{slidesPerView:4,slidesOffsetAfter:0},0:{slidesPerView:"auto",slidesOffsetAfter:16}}})}function findProductById(id){for(const product of allRecommendProductData)if(product.title&&product.id===id)return product;return null}function addSelectItemEvent(){const items=document.querySelectorAll(".recommend-swiper .product-item");items.length>0&&items.forEach((item,idx)=>{const itemImg=item.querySelector(".product-item--image");itemImg.addEventListener("click",()=>{let itemListName="\uBA54\uC778_RECOMMEND";window.pageType!="\uBA54\uC778"&&(itemListName="\uC81C\uD488 \uC0C1\uC138_RECOMMEND");const itemName=item.querySelector(".product-item--title").textContent,imgFileName=itemImg.querySelector("img").src.split("/").pop();dataLayer.push({ecommerce:null}),window.dataLayer.push({event:"select_item",page_type:window.pageType,ecommerce:{items:[{item_list_name:itemListName,item_name:itemName,img_url:imgFileName,index:idx+1}]}})})})}
//# sourceMappingURL=/cdn/shop/t/152/assets/section-recommend.js.map
