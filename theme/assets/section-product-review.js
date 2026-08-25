const productOptions=[...variantsAllOptionData];let productReviews=[],currentPage=1;const reviewsPerPage=5;let activeHeightFilter={min:null,max:null},activeWeightFilter={min:null,max:null};const REVIEW_LOADING_MESSAGE="\uB9AC\uBDF0 \uC815\uBCF4\uB97C \uBD88\uB7EC\uC624\uB294 \uC911\uC785\uB2C8\uB2E4.",REVIEW_ERROR_MESSAGE="\uB9AC\uBDF0 \uC815\uBCF4\uB97C \uBD88\uB7EC\uC62C \uC218 \uC5C6\uC2B5\uB2C8\uB2E4. \uC7A0\uC2DC \uD6C4 \uB2E4\uC2DC \uC2DC\uB3C4\uD574 \uC8FC\uC138\uC694.";function toIsoStringSafe(dateValue){const d=new Date(dateValue);return Number.isNaN(d.getTime())?null:d.toISOString()}function buildReviewSchemaPayload(){if(!Array.isArray(productReviews)||productReviews.length===0)return null;const validStars=productReviews.map(r=>Number(r.stars)).filter(v=>Number.isFinite(v)&&v>0);if(validStars.length===0)return null;const ratingValue=validStars.reduce((sum,v)=>sum+v,0)/validStars.length,reviewCount=productReviews.length,primarySku=Array.isArray(productSkus)&&productSkus[0]?productSkus[0]:void 0,productUrl=typeof location<"u"?location.href:void 0,reviews=productReviews.map(r=>{const author=(r.customer_name||"").trim()||"Anonymous",published=toIsoStringSafe(r.created_at);return{"@type":"Review",name:`Review by ${author}`,author:{"@type":"Person",name:author},reviewBody:r.text||"",datePublished:published||void 0,reviewRating:{"@type":"Rating",ratingValue:Number.isFinite(r.stars)?r.stars:0,bestRating:5,worstRating:1},itemReviewed:{"@type":"Product",name:productName,sku:r.product_sku||primarySku||void 0},identifier:r.review_id||void 0,url:productUrl}}).filter(r=>r.reviewRating&&Number(r.reviewRating.ratingValue)>0);return reviews.length===0?null:{"@context":"https://schema.org","@type":"Product",name:productName,sku:primarySku||void 0,url:productUrl,aggregateRating:{"@type":"AggregateRating",ratingValue:Number(ratingValue.toFixed(2)),reviewCount,bestRating:5,worstRating:1},review:reviews}}function injectReviewSchema(){try{const payload=buildReviewSchemaPayload();if(!payload)return;const scripts=[...document.querySelectorAll('script[type="application/ld+json"]')];let patched=!1;for(const s of scripts){const raw=s.textContent.trim();if(!raw)continue;let data;try{data=JSON.parse(raw)}catch{continue}const arr=Array.isArray(data)?data:[data];let touched=!1;const patchedArr=arr.map(item=>{if(item&&item["@type"]==="Product"){const merged={...item};return merged.aggregateRating=payload.aggregateRating,merged.review=payload.review,patched=!0,touched=!0,merged}return item});if(touched){s.textContent=JSON.stringify(Array.isArray(data)?patchedArr:patchedArr[0]);break}}if(!patched){const scriptId="dynamic-review-schema",existing=document.getElementById(scriptId);existing&&existing.parentNode&&existing.parentNode.removeChild(existing);const script=document.createElement("script");script.id=scriptId,script.type="application/ld+json",script.textContent=JSON.stringify(payload),document.head.appendChild(script)}}catch(error){console.warn("[Product Review] Failed to inject review schema",error)}}function setProductReviewLoading(isLoading,message){const loadingEl=document.querySelector(".product-review-loading");loadingEl&&(message?loadingEl.textContent=message:isLoading||(loadingEl.textContent=REVIEW_LOADING_MESSAGE),isLoading?loadingEl.classList.remove("hidden"):loadingEl.classList.add("hidden"))}function toggleReviewContentVisibility(show){[document.querySelector(".review-option-wrapper"),document.querySelector(".review-controller"),document.querySelector(".review-items"),document.querySelector(".review-pagination"),document.querySelector(".best_review_box")].forEach(el=>{el&&(show?el.classList.remove("hidden"):el.classList.add("hidden"))})}function getProductFromUrl(){return window.location.pathname.split("/")[2]}function getFilteredReviews(){return productReviews.filter(productReview=>{const matchesHeight=(activeHeightFilter.min===null||productReview.customer_height>=activeHeightFilter.min)&&(activeHeightFilter.max===null||productReview.customer_height<=activeHeightFilter.max),matchesWeight=(activeWeightFilter.min===null||productReview.customer_weight>=activeWeightFilter.min)&&(activeWeightFilter.max===null||productReview.customer_weight<=activeWeightFilter.max);return matchesHeight&&matchesWeight})}function getPaginatedReviews(){const filteredReviews=getFilteredReviews(),startIndex=(currentPage-1)*reviewsPerPage,endIndex=startIndex+reviewsPerPage;return filteredReviews.slice(startIndex,endIndex)}function renderPagination(){const filteredReviews=getFilteredReviews(),totalPages=Math.ceil(filteredReviews.length/reviewsPerPage);let paginationHTML="";if(paginationHTML+=`
        <button class="review-pagination-btn prev ${currentPage===1?"disabled":""}" data-page="${currentPage-1}">
            <svg xmlns="http://www.w3.org/2000/svg" width="12" height="8" viewBox="0 0 12 8" fill="none">
                <path d="M1.1875 1.8125L6 6.625L10.8125 1.8125" stroke="black" stroke-width="1.2" stroke-linecap="square"></path>
            </svg>
        </button>
    `,totalPages<=7)for(let i=1;i<=totalPages;i++)paginationHTML+=`<button class="review-pagination-btn ${currentPage===i?"active":""}" data-page="${i}">${i}</button>`;else{paginationHTML+=`<button class="review-pagination-btn ${currentPage===1?"active":""}" data-page="1">1</button>`,currentPage>4&&(paginationHTML+='<button class="review-pagination-btn disabled">...</button>');let startPage=Math.max(2,currentPage-1),endPage=Math.min(totalPages-1,currentPage+1);currentPage<=4?(startPage=2,endPage=5):currentPage>=totalPages-3&&(startPage=totalPages-4,endPage=totalPages-1);for(let i=startPage;i<=endPage;i++)paginationHTML+=`<button class="review-pagination-btn ${currentPage===i?"active":""}" data-page="${i}">${i}</button>`;currentPage<totalPages-3&&(paginationHTML+='<button class="review-pagination-btn disabled">...</button>'),paginationHTML+=`<button class="review-pagination-btn ${currentPage===totalPages?"active":""}" data-page="${totalPages}">${totalPages}</button>`}paginationHTML+=`
        <button class="review-pagination-btn next ${currentPage===totalPages?"disabled":""}" data-page="${currentPage+1}">
            <svg xmlns="http://www.w3.org/2000/svg" width="12" height="8" viewBox="0 0 12 8" fill="none">
                <path d="M1.1875 1.8125L6 6.625L10.8125 1.8125" stroke="black" stroke-width="1.2" stroke-linecap="square"></path>
            </svg>
        </button>
    `,document.querySelector(".review-pagination").innerHTML=paginationHTML,document.querySelectorAll(".review-pagination-btn").forEach(button=>{button.addEventListener("click",e=>{const targetPage=Number(e.currentTarget.dataset.page);if(!isNaN(targetPage)&&targetPage>=1&&targetPage<=totalPages){currentPage=targetPage,updateReviewHTML(),detailReviewModal();const reviewOptionWrapper=document.querySelector(".review-option-wrapper");if(reviewOptionWrapper){const elementPosition=reviewOptionWrapper.getBoundingClientRect().top,scrollPosition=document.documentElement&&document.documentElement.scrollTop||document.body.scrollTop||0,offsetPosition=elementPosition+scrollPosition-100;window.scrollTo({top:offsetPosition,behavior:"smooth"})}}})})}function formatNumberWithCommas(number){return Number(number).toLocaleString()}function formatDate(dateString){const date=new Date(dateString),year=date.getFullYear(),month=String(date.getMonth()+1).padStart(2,"0"),day=String(date.getDate()).padStart(2,"0");return`${year}.${month}.${day}`}async function capturePreviewFromVideoUrl(videoUrl){return new Promise((resolve,reject)=>{const tempVideo=document.createElement("video");tempVideo.crossOrigin="anonymous",tempVideo.playsInline=!0,tempVideo.muted=!0,tempVideo.preload="metadata";let captured=!1,attemptIndex=0,candidateTimes=[1,2];const cleanup=()=>{tempVideo.pause(),tempVideo.removeAttribute("src"),tempVideo.load(),tempVideo.remove()},buildCandidateTimes=duration=>{const times=[];if(Number.isFinite(duration)&&duration>0){const safeDuration=Math.min(duration,12);times.push(Math.min(1,safeDuration)),times.push(Math.min(2,safeDuration)),times.push(Math.min(Math.max(safeDuration*.25,.5),safeDuration)),times.push(Math.min(Math.max(safeDuration*.5,1),safeDuration)),times.push(Math.min(Math.max(safeDuration*.75,1.5),safeDuration))}return Array.from(new Set(times)).sort((a,b)=>a-b)},isMostlyBlack=(ctx,width,height)=>{try{const sampleWidth=Math.max(1,Math.min(160,width)),sampleHeight=Math.max(1,Math.min(160,height)),imageData=ctx.getImageData(0,0,sampleWidth,sampleHeight).data;let sum=0;for(let i=0;i<imageData.length;i+=4)sum+=imageData[i]+imageData[i+1]+imageData[i+2];return sum/(sampleWidth*sampleHeight*3)<8}catch{return!1}},captureFrame=()=>{if(!captured){captured=!0;try{const canvas=document.createElement("canvas"),width=tempVideo.videoWidth||1,height=tempVideo.videoHeight||1;canvas.width=width,canvas.height=height;const ctx=canvas.getContext("2d");if(ctx.drawImage(tempVideo,0,0,width,height),isMostlyBlack(ctx,width,height)&&candidateTimes[attemptIndex]){captured=!1,attemptIndex+=1,seekToCandidate();return}const dataURL=canvas.toDataURL("image/jpeg");cleanup(),resolve(dataURL)}catch(error){cleanup(),reject(error)}}},seekToCandidate=()=>{const targetTime=candidateTimes[attemptIndex];if(targetTime===void 0){captureFrame();return}try{tempVideo.currentTime=targetTime}catch{captureFrame()}};tempVideo.addEventListener("seeked",captureFrame),tempVideo.addEventListener("loadedmetadata",()=>{const duration=tempVideo.duration;candidateTimes=buildCandidateTimes(duration),attemptIndex=0,seekToCandidate()},{once:!0}),tempVideo.addEventListener("loadeddata",()=>{captured||captureFrame()}),tempVideo.addEventListener("error",error=>{cleanup(),reject(error)},{once:!0}),tempVideo.src=videoUrl,tempVideo.load()})}function populateMissingVideoPreviews(scopeSelector=".review_video_wrapper"){document.querySelectorAll(scopeSelector).forEach(wrapper=>{const img=wrapper.querySelector(".review_video_preview"),video=wrapper.querySelector("video"),hasImgSrc=img&&img.getAttribute("src"),alreadyFilled=img&&img.dataset.previewFilled==="true";if(!img||!video||alreadyFilled)return;if(hasImgSrc){img.dataset.previewFilled="true";return}const source=video.querySelector("source"),videoUrl=source?source.getAttribute("src"):null;videoUrl&&(img.dataset.previewFilled="true",capturePreviewFromVideoUrl(videoUrl).then(dataUrl=>{img.src=dataUrl}).catch(()=>{img.dataset.previewFilled="false"}))})}function maskLastFourChar(name){if(name==="\uB124\uC774\uBC84 \uB9AC\uBDF0")return name;let nameLength=name.length,maskingName="";if(nameLength===3)return maskingName=name.substring(0,1)+"**",maskingName;if(nameLength>3){let maskLength=Math.floor(nameLength/2),visibleLength=nameLength-maskLength,visiblePart=name.substring(0,visibleLength),maskedPart="*".repeat(maskLength);return maskingName=visiblePart+maskedPart,maskingName}return name}function skuOptionFilter(sku){const filteredOptions=productOptions.filter(option=>option.sku===sku);return filteredOptions.length>0?filteredOptions[0].options:null}async function fetchLikeCount(){let reviewIds=[];productReviews.forEach(function(el){el?.review_id&&reviewIds.push(el.review_id)});try{const response=await fetch("https://sidiz-shopify.sidiz.com/review/like/list",{method:"POST",headers:{Accept:"application/json","Content-Type":"application/json"},body:JSON.stringify({review_ids:reviewIds,customerMd5Hash})});if(!response.ok){if(response.status===404)return null;throw new Error(`API \uC694\uCCAD \uC2E4\uD328: ${response.status} ${response.statusText}`)}const data=await response.json();if(!data||!data.data||!Array.isArray(data.data))throw new Error("\uC798\uBABB\uB41C \uC751\uB2F5 \uB370\uC774\uD130 \uD615\uC2DD");return data.data.forEach(el=>{const review=productReviews.find(r=>r.review_id==el.review_id);review&&(review.rec_cnt=el.like_cnt?el.like_cnt:0,review.is_liked=el.liked_by_customer)}),data}catch{return null}}function updateReviewHTML(){let reviewHTML="";const paginatedReviews=getPaginatedReviews();paginatedReviews.length===0?reviewHTML='<div class="no-reviews-message">\uC791\uC131\uB41C \uB9AC\uBDF0\uAC00 \uC5C6\uC2B5\uB2C8\uB2E4.</div>':paginatedReviews.forEach((review,idx)=>{let userName=maskLastFourChar(review.customer_name),createDate=formatDate(review.created_at),optTagArr=[];if(review.product_sku){let options=skuOptionFilter(review.product_sku);options&&options.length>0&&options.map(option=>{optTagArr.push(`
                        <div class="product_option-value caption-1">
                          <p>${option.name}</p>
                          <p>${option.value}</p>
                        </div>
                        `)})}let reviewId=review.review_id.replace(/\D/g,""),imageList=[],videoList=[];review.media_list&&review.media_list.length>0&&review.media_list.forEach(media=>{typeof media=="string"?imageList.push(media):videoList.push(media)});const reviewCustomerId=review.customer?review.customer.split("/").pop():null;let md5ReviewCustomerId=CryptoJS.MD5(reviewCustomerId).toString(),canRecomedFlg=reviewCustomerId===null||md5ReviewCustomerId!==String(customerMd5Hash);reviewHTML+=`
              <div class="review_item_wrapper gtm-review-item" data-h="${review.customer_height}" data-w="${review.customer_weight}" data-idx="${idx}">
                <div class="review_item_basic">
                  <div class="review_info">
                    <div class="review_rate">
                      ${[...Array(5)].map((_,i)=>`
                        <div>
                            <img src="${i<review.stars?icon_star_solid_bk:icon_star_line_bk}" alt="">
                        </div>
                      `).join("")}
                    </div>

                    <div class="review_writer_info">
                        <div class="review_writer">${userName}</div>
                        <div class="writer_info_wrapper">
                            <div class="writer_info ${review.customer_height?"":"hidden"}"><p class="info_key">\uD0A4</p><p class="info_value">${review.customer_height?`${review.customer_height}cm`:""}</p></div>
                            <div class="writer_info ${review.customer_weight?"":"hidden"}"><p class="info_key">\uBAB8\uBB34\uAC8C</p><p class="info_value">${review.customer_weight?`${review.customer_weight}kg`:""}</p></div>
                        </div>
                        
                        <div class="product_option">
                            ${optTagArr.length>0?optTagArr.join(`
                            <div style="display:flex; padding:4px;">
                                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 14 14" fill="none">
                                    <g clip-path="url(#clip0_8109_285332)">
                                    <rect x="6.39844" y="0.5" width="1.2" height="14" fill="#D6DADE"></rect>
                                    </g>
                                    <defs>
                                    <clipPath id="clip0_8109_285332">
                                        <rect width="14" height="14" fill="white" transform="translate(0 0.5)"></rect>
                                    </clipPath>
                                    </defs>
                                </svg>
                            </div>
                            `):""}
                        </div>
                    </div>
                  </div>

                  <div class="review_content">
                    <div class="review_content_text_wrapper">
                        <div class="content_richtext">${review.text}</div>
                    </div>
                    <div class="review_img_container">
                        <div class="review_img_wrapper">
                        ${imageList&&imageList.length>0?imageList.map(image=>image?`<img src="${image}" alt="\uB9AC\uBDF0 \uC774\uBBF8\uC9C0" class="review_img" loading="lazy" data-idx="${idx}">`:"").join(""):""}
                        ${videoList&&videoList.length>0?videoList.map(video=>{let sources=video.sources.map(source=>`<source src="${source.url}" type="${source.mime_type}">`).join("");return`
                                    <div class="review_video_wrapper">
                                        <img src="${video.preview_image?.src||""}"
                                             alt="\uBE44\uB514\uC624 \uD504\uB9AC\uBDF0"
                                             loading="lazy"
                                             class="review_video_preview">
                                        <video controls class="review_video">
                                            ${sources}
                                        </video>
                                    </div>
                                `}).join(""):""}
                        </div>
                    </div>
                  </div>
                </div>

                <div class="review_recommend">
                  <div class="recommend_btn ${review.is_liked?"selected":""}" onclick="toggleRecommendBtn(event)" data-review_stat="${review.is_liked}" data-review_id="${reviewId}" data-recommend="${canRecomedFlg}">
                    <img src="${icon_like}" alt="">
                    <div class="recommend-count caption-2">${review.rec_cnt?formatNumberWithCommas(review.rec_cnt):0}</div>
                  </div>
                  <div class="regi_date">
                    ${createDate}
                  </div>
                </div>
              </div>
            `}),document.querySelector(".review-items").innerHTML=reviewHTML,paginatedReviews.length>0&&renderPagination(),populateMissingVideoPreviews(".review_video_wrapper"),scheduleMoreButtons()}function updateBestReviewHTML(){const bestReviewCount=liquidBestReviewCount;let finalReviews=productReviews.sort((a,b)=>b.rec_cnt-a.rec_cnt).slice(0,bestReviewCount);const bestReviewBox=document.querySelector(".best_review_box");if(finalReviews.length<2){bestReviewBox.style.display="none";return}else bestReviewBox.style.display="block";let reviewHTML="";finalReviews.slice(0,3).forEach((review,idx)=>{let userName=maskLastFourChar(review.customer_name),createDate=formatDate(review.created_at),optTagArr=[];if(review.product_sku){let options=skuOptionFilter(review.product_sku);options&&options.length>0&&options.map(option=>{optTagArr.push(`
                        <div class="product_option-value caption-1">
                          <p>${option.name}</p>
                          <p>${option.value}</p>
                        </div>
                        `)})}let reviewId=review.review_id.replace(/\D/g,""),imageList=[],videoList=[];review.media_list&&review.media_list.length>0&&review.media_list.forEach(media=>{typeof media=="string"?imageList.push(media):videoList.push(media)});const reviewCustomerId=review.customer?review.customer.split("/").pop():null;let md5ReviewCustomerId=CryptoJS.MD5(reviewCustomerId).toString(),canRecomedFlg=reviewCustomerId===null||md5ReviewCustomerId!==String(customerMd5Hash);reviewHTML+=`
        <div class="best-review gtm-review-item" data-idx="${idx}">
            <div class="best_review_wrapper">
                <div class=best-review-info>
                    <div class="review_rate">
                        ${[...Array(5)].map((_,i)=>`
                            <div>
                                <img src="${i<review.stars?icon_star_solid_bk:icon_star_line_bk}" alt="">
                            </div>`).join("")}
                    </div>

                    <div class="review_writer_info">
                        <div class="review_writer">${userName}</div>
                        <div class="writer_info_wrapper">
                            <div class="writer_info ${review.customer_height?"":"hidden"}"><p class="info_key">\uD0A4</p><p class="info_value">${review.customer_height?`${review.customer_height}cm`:""}</p></div>
                            <div class="writer_info ${review.customer_weight?"":"hidden"}"><p class="info_key">\uBAB8\uBB34\uAC8C</p><p class="info_value">${review.customer_weight?`${review.customer_weight}kg`:""}</p></div>
                        </div>
                        <div class="product_option">
                        ${optTagArr.length>0?optTagArr.join(`
                            <div style="display:flex; padding:4px;">
                                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 14 14" fill="none">
                                    <g clip-path="url(#clip0_8109_285332)">
                                    <rect x="6.39844" y="0.5" width="1.2" height="14" fill="#D6DADE"></rect>
                                    </g>
                                    <defs>
                                    <clipPath id="clip0_8109_285332">
                                        <rect width="14" height="14" fill="white" transform="translate(0 0.5)"></rect>
                                    </clipPath>
                                    </defs>
                                </svg>
                            </div>
                            `):""}
                      </div>
                    </div>
                </div>

                <div class="best-review_content">
                    <div class="review_content_text_wrapper">
                        <div class="best-review-richtext">${review.text}</div>
                    </div>
                    <div class="review_img_container">
                        <div class="review_img_wrapper">
                        ${imageList&&imageList.length>0?imageList.map(image=>image?`<img src="${image}" alt="\uB9AC\uBDF0 \uC774\uBBF8\uC9C0" class="review_img" data-idx="${idx}">`:"").join(""):""}
                        ${videoList&&videoList.length>0?videoList.map(video=>{let sources=video.sources.map(source=>`<source src="${source.url}" type="${source.mime_type}">`).join("");return`
                                    <div class="review_video_wrapper">
                                        <img src="${video.preview_image?.src||""}" 
                                             alt="\uBE44\uB514\uC624 \uD504\uB9AC\uBDF0" 
                                             class="review_video_preview">
                                        <video controls class="review_video">
                                            ${sources}
                                        </video>
                                    </div>
                                `}).join(""):""}
                        </div>
                    </div>
                </div>
            </div>

            <div class="best-review_recommend">
                <div class="recommend_btn ${review.is_liked?"selected":""}" onclick="toggleRecommendBtn(event)" data-review_stat="${review.is_liked}" data-review_id="${reviewId}" data-recommend="${canRecomedFlg}">
                    <img src="${icon_like}" alt="">
                    <div class="recommend-count caption-2">${review.rec_cnt?formatNumberWithCommas(review.rec_cnt):0}</div>
                </div>
                <div class="regi_date">
                    ${createDate}
                </div>
            </div>
        </div>
        `}),document.querySelector(".best-review-wrapper").innerHTML=reviewHTML,populateMissingVideoPreviews(".best-review .review_video_wrapper"),scheduleMoreButtons(3,".best-review-richtext")}function toggleRecommendBtn(event){event.stopPropagation();const parentTarget=event.currentTarget,reviewId=parentTarget.dataset.review_id,reviewStat=parentTarget.dataset.review_stat,userCanRecommnedFlg=parentTarget.dataset.recommend;customerMd5Hash?userCanRecommnedFlg=="true"?fetch("https://sidiz-shopify.sidiz.com/review/like/toggle",{method:"POST",headers:{Accept:"application/json","Content-Type":"application/json"},body:JSON.stringify({review_id:`gid://shopify/Metaobject/${reviewId}`,customerMd5Hash})}).then(response=>{if(!response.ok)throw new Error(`HTTP error! status: ${response.status}`);return response.json()}).then(data=>{if(data.code=="0"&&data.success===!0){let likeFlg=data.data.isLiked,likeCnt=data.data.like_count;updateLikeCountUI(reviewId,likeCnt,likeFlg),updateProductReviewsRecCnt(reviewId,likeCnt,likeFlg)}else if(data.code=="1001")openMiniModalWithContent(`
                            <div class="review_err_modal body-1" style="text-align:center;">
                                \uC120\uD0DD\uD558\uC2E0 \uB9AC\uBDF0\uAC00 \uC5C6\uAC70\uB098 \uB85C\uADF8\uC778\uC774 \uD544\uC694\uD569\uB2C8\uB2E4.<br>
                                \uB2E4\uC2DC \uC2DC\uB3C4\uD574 \uC8FC\uC138\uC694.
                                <div>Error Code : 1001</div>
                                <div class="close_btn border_basic2 body-3">\uB2EB\uAE30</div>
                            </div>
                        `,function(){const alertModal=document.querySelector("#site-alert-modal");document.querySelector(".close_btn").addEventListener("click",()=>{closeMiniModal(),alertModal&&closeAlertModal()})});else{let modalContent=`
                            <div class="review_err_modal body-1" style="text-align:center;">
                                \uC2DC\uC2A4\uD15C \uC624\uB958\uAC00 \uBC1C\uC0DD\uD588\uC2B5\uB2C8\uB2E4. \uB2E4\uC2DC \uC2DC\uB3C4\uD574 \uC8FC\uC138\uC694.<br>
                                \uBB38\uC81C\uAC00 \uC9C0\uC18D\uB420 \uACBD\uC6B0 \uCC57\uBD07 \uB610\uB294 \uCEE8\uD0DD\uC13C\uD130\uB85C \uBB38\uC758 \uD574 \uC8FC\uC2DC\uAE30 \uBC14\uB78D\uB2C8\uB2E4.
                                <div>Error Code : ${data.code}</div>
                                <div class="close_btn border_basic2 body-3">\uB2EB\uAE30</div>
                            </div>
                        `;openMiniModalWithContent(modalContent,function(){const alertModal=document.querySelector("#site-alert-modal");document.querySelector(".close_btn").addEventListener("click",()=>{closeMiniModal(),alertModal&&closeAlertModal()})})}}).catch(error=>{let modalContent=`
                        <div class="review_err_modal body-1" style="text-align:center;">
                            \uC2DC\uC2A4\uD15C \uC624\uB958\uAC00 \uBC1C\uC0DD\uD588\uC2B5\uB2C8\uB2E4. \uB2E4\uC2DC \uC2DC\uB3C4\uD574 \uC8FC\uC138\uC694.<br>
                            \uBB38\uC81C\uAC00 \uC9C0\uC18D\uB420 \uACBD\uC6B0 \uCC57\uBD07 \uB610\uB294 \uCEE8\uD0DD\uC13C\uD130\uB85C \uBB38\uC758 \uD574 \uC8FC\uC2DC\uAE30 \uBC14\uB78D\uB2C8\uB2E4.
                            <div>Error Code : ${error.code}</div>
                            <div class="close_btn border_basic2 body-3">\uB2EB\uAE30</div>
                        </div>
                    `;return openMiniModalWithContent(modalContent,function(){const alertModal=document.querySelector("#site-alert-modal");document.querySelector(".close_btn").addEventListener("click",()=>{closeMiniModal(),alertModal&&closeAlertModal()})}),!1}):openMiniModalWithContent(`
                <div class="review_err_modal body-1" style="text-align:center;">
                    \uBCF8\uC778\uC774 \uC791\uC131\uD55C \uB9AC\uBDF0\uB294 \uCD94\uCC9C\uD560 \uC218 \uC5C6\uC2B5\uB2C8\uB2E4.
                    <div class="close_btn border_basic2 body-3">\uB2EB\uAE30</div>
                </div>
            `,function(){const alertModal=document.querySelector("#site-alert-modal");document.querySelector(".close_btn").addEventListener("click",()=>{closeMiniModal(),alertModal&&closeAlertModal()})}):commonLoginModal()}function updateLikeCountUI(reviewId,newLikeCount,likeFlg){document.querySelectorAll(`.recommend_btn[data-review_id="${reviewId}"]`).forEach(button=>{const countElement=button.querySelector(".recommend-count");countElement&&(countElement.textContent=formatNumberWithCommas(newLikeCount)),likeFlg==!0?button.classList.add("selected"):button.classList.remove("selected")})}function updateProductReviewsRecCnt(reviewId,likeCnt,likeFlg){if(typeof productReviews<"u"&&Array.isArray(productReviews)){for(let i=0;i<productReviews.length;i++)if(productReviews[i].review_id.replace("gid://shopify/Metaobject/","")===reviewId){productReviews[i].rec_cnt=likeCnt,productReviews[i].is_liked=likeFlg;return}}}function setupFilters(){document.querySelectorAll(".height-option-btn").forEach(button=>{button.addEventListener("click",()=>{button.classList.contains("active-filter")?(activeHeightFilter={min:null,max:null},button.classList.remove("active-filter")):(activeHeightFilter={min:Number(button.dataset.minh),max:Number(button.dataset.maxh)},document.querySelectorAll(".height-option-btn").forEach(btn=>{btn.classList.remove("active-filter")}),button.classList.add("active-filter")),currentPage=1,updateReviewHTML(),detailReviewModal(),document.querySelector(".total-review_count p:last-child").textContent=getFilteredReviewCount()})}),document.querySelectorAll(".weight-option-btn").forEach(button=>{button.addEventListener("click",()=>{button.classList.contains("active-filter")?(activeWeightFilter={min:null,max:null},button.classList.remove("active-filter")):(activeWeightFilter={min:Number(button.dataset.minw),max:Number(button.dataset.maxw)},document.querySelectorAll(".weight-option-btn").forEach(btn=>{btn.classList.remove("active-filter")}),button.classList.add("active-filter")),currentPage=1,updateReviewHTML(),detailReviewModal(),document.querySelector(".total-review_count p:last-child").textContent=getFilteredReviewCount()})})}function getFilteredReviewCount(){return getFilteredReviews().length.toLocaleString()}function initialize(){productReviews.sort((a,b)=>b.rec_cnt!==a.rec_cnt?b.rec_cnt-a.rec_cnt:new Date(b.created_at)-new Date(a.created_at)),setupFilters(),updateReviewHTML(),document.querySelector(".total-review_count p:last-child").textContent=getFilteredReviewCount()}document.addEventListener("DOMContentLoaded",async()=>{setProductReviewLoading(!0,REVIEW_LOADING_MESSAGE),toggleReviewContentVisibility(!1);try{window.productReviewLoaded&&await window.productReviewLoaded,Array.isArray(window.allProductReviewData)?productReviews=window.allProductReviewData:productReviews=[]}catch(error){console.error("[Product Review] Failed to initialize reviews",error),setProductReviewLoading(!0,REVIEW_ERROR_MESSAGE);return}document.querySelector(".orderBy-recommended").classList.add("active"),document.querySelector(".orderBy-latest").classList.remove("active"),await fetchLikeCount(),initialize(),updateBestReviewHTML(),detailReviewModal(),injectReviewSchema(),setProductReviewLoading(!1),toggleReviewContentVisibility(!0)}),document.querySelector(".orderBy-recommended").addEventListener("click",()=>{productReviews.sort((a,b)=>b.rec_cnt-a.rec_cnt),currentPage=1,updateReviewHTML(),detailReviewModal(),document.querySelector(".orderBy-recommended").classList.add("active"),document.querySelector(".orderBy-latest").classList.remove("active")}),document.querySelector(".orderBy-latest").addEventListener("click",()=>{productReviews.sort((a,b)=>new Date(b.created_at)-new Date(a.created_at)),currentPage=1,updateReviewHTML(),detailReviewModal(),document.querySelector(".orderBy-latest").classList.add("active"),document.querySelector(".orderBy-recommended").classList.remove("active")});function scheduleMoreButtons(maxLines=2,selector=".content_richtext"){requestAnimationFrame(()=>{requestAnimationFrame(()=>addMoreButtons(maxLines,selector))})}function addMoreButtons(maxLines=2,selector=".content_richtext"){document.querySelectorAll(selector).forEach(content=>{const existingBtn=content.parentElement.querySelector(".moreBtn");existingBtn&&existingBtn.remove();const computedStyle=window.getComputedStyle(content),lineHeight=parseFloat(computedStyle.lineHeight);if(!lineHeight)return;const maxHeight=lineHeight*maxLines,computedClamp=computedStyle.getPropertyValue("-webkit-line-clamp"),inlineClamp=content.style.getPropertyValue("-webkit-line-clamp"),activeClamp=inlineClamp||computedClamp||`${maxLines}`,originalStyles={display:content.style.display,clamp:inlineClamp,maxHeight:content.style.maxHeight,overflow:content.style.overflow,position:content.style.position},initialHeight=content.getBoundingClientRect().height;content.style.setProperty("-webkit-line-clamp","unset"),content.style.display="block",content.style.maxHeight="",content.style.overflow="visible";const fullHeight=content.scrollHeight;if(content.style.setProperty("-webkit-line-clamp",activeClamp),content.style.display="-webkit-box",content.style.maxHeight=`${maxHeight}px`,content.style.overflow="hidden",!(fullHeight>initialHeight+1)){content.style.maxHeight=originalStyles.maxHeight||"",content.style.overflow=originalStyles.overflow||"",content.style.display=originalStyles.display||"",inlineClamp?content.style.setProperty("-webkit-line-clamp",inlineClamp):computedClamp?content.style.setProperty("-webkit-line-clamp",computedClamp):content.style.removeProperty("-webkit-line-clamp");return}content.style.position="relative";const moreBtn=document.createElement("div");moreBtn.classList.add("moreBtn"),moreBtn.setAttribute("data-toggle_status","F"),moreBtn.innerHTML=`
            \uB354\uBCF4\uAE30
            <svg xmlns="http://www.w3.org/2000/svg" width="12" height="8" viewBox="0 0 12 8" fill="none">
                <path d="M1.1875 1.8125L6 6.625L10.8125 1.8125" stroke="black" stroke-width="1.2" stroke-linecap="square"/>
            </svg>
        `,content.parentElement.appendChild(moreBtn),moreBtn.addEventListener("click",()=>{if(moreBtn.dataset.toggle_status==="F"){content.style.setProperty("-webkit-line-clamp","unset"),content.style.display="block",content.style.maxHeight="",content.style.overflow="visible",content.style.position=originalStyles.position||"relative",moreBtn.innerHTML=`
                    \uC811\uAE30
                    <svg xmlns="http://www.w3.org/2000/svg" width="12" height="8" viewBox="0 0 12 8" fill="none">
                        <path d="M1.1875 6.1875L6 1.375L10.8125 6.1875" stroke="black" stroke-width="1.2" stroke-linecap="square"/>
                    </svg>
                `,moreBtn.dataset.toggle_status="T";let reviewItem=moreBtn.closest(".gtm-review-item"),reviewIdx=Number(reviewItem.dataset.idx)+1,clickType="";reviewItem.classList.contains("best-review")?clickType="\uBCA0\uC2A4\uD2B8 \uB9AC\uBDF0":(clickType="\uC77C\uBC18 \uB9AC\uBDF0",reviewIdx=getReviewIdx(reviewIdx)),window.dataLayer.push({event:"click_review",page_type:"\uC81C\uD488 \uC0C1\uC138",click_type:clickType,click_text:"\uB354\uBCF4\uAE30",index:reviewIdx})}else content.style.setProperty("-webkit-line-clamp",`${maxLines}`),content.style.display="-webkit-box",content.style.maxHeight=`${maxHeight}px`,content.style.overflow="hidden",content.style.position="relative",moreBtn.innerHTML=`
                    \uB354\uBCF4\uAE30
                    <svg xmlns="http://www.w3.org/2000/svg" width="12" height="8" viewBox="0 0 12 8" fill="none">
                        <path d="M1.1875 1.8125L6 6.625L10.8125 1.8125" stroke="black" stroke-width="1.2" stroke-linecap="square"/>
                    </svg>
                `,moreBtn.dataset.toggle_status="F"})})}function detailReviewModal(){const reviewContainer=document.querySelector("#prod_detail_review");if(!reviewContainer)return;let bestReviewWrapper=reviewContainer.querySelector(".best-review-wrapper");if(bestReviewWrapper){const bestReviews=bestReviewWrapper.querySelectorAll(".best-review");addAllImagesClickListener(bestReviews)}let reviewItems=reviewContainer.querySelector(".review-items");if(reviewItems){const reviewDetails=reviewItems.querySelectorAll(".review_item_wrapper");addAllImagesClickListener(reviewDetails)}function addAllImagesClickListener(reviews){reviews.forEach(review=>{review.querySelectorAll(".review_img_wrapper").forEach(wrapper=>{wrapper.querySelectorAll("img").forEach(img=>{img.style.cursor="pointer",img.addEventListener("click",function(){let reviewItem=img.closest(".gtm-review-item"),reviewIdx=Number(reviewItem.dataset.idx)+1,clickType="";reviewItem.classList.contains("best-review")?clickType="\uBCA0\uC2A4\uD2B8 \uB9AC\uBDF0":(clickType="\uC77C\uBC18 \uB9AC\uBDF0",reviewIdx=getReviewIdx(reviewIdx)),window.dataLayer.push({event:"click_review",page_type:"\uC81C\uD488 \uC0C1\uC138",click_type:clickType,click_text:"\uB9AC\uBDF0 \uC774\uBBF8\uC9C0",index:reviewIdx});let modalContent=`
                <div class="modal_detail_review">
                  ${review.innerHTML}
                </div>
              `;openModalWithContent("",modalContent,()=>{})})})})})}}function getReviewIdx(idx){return(Number(document.querySelector(".review-pagination .active").dataset.page)-1)*5+idx}
//# sourceMappingURL=/cdn/shop/t/152/assets/section-product-review.js.map
