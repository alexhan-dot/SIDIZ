let product_table=null;function formatListCardDesc(text){return text?String(text).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#39;").replace(/\r?\n/g,"<br>"):""}window.addEventListener("load",()=>{if(new URLSearchParams(window.location.search).get("ezRepairSearch")==="true"){const newUrl=new URL(window.location.href);newUrl.searchParams.delete("ezRepairSearch"),window.history.replaceState({},"",newUrl),loadAndOpenModal()}}),document.addEventListener("DOMContentLoaded",async()=>{try{await allEasyrepairDataLoaded}catch(error){console.error("Error loading data:",error)}document.querySelector(".easy-repair--search .input-container input").value.trim()!=""&&document.querySelector("#clear-btn").classList.remove("hidden"),document.querySelector("#search-btn").addEventListener("click",function(){const inputValue=document.querySelector(".easy-repair--search .input-container input").value;sessionStorage.setItem("easyRepairSearch","T"),window.location.href=`/pages/easy-repair?prodCode=${inputValue}`});let inputContainer=document.querySelector(".easy-repair--search .input-container");inputContainer.querySelector("input").addEventListener("keydown",event=>{event.key==="Enter"&&inputContainer.querySelector(".search-btn").click()}),howtocheckBadgeModal(),document.querySelector(".easy-repair--search .tag.my-prod-verify").addEventListener("click",()=>{customerMd5Hash?loadAndOpenModal():commonLoginModal("ezRepairSearch")});const prevAdditionalAction=sessionStorage.getItem("prev_additional_action"),saveModal=sessionStorage.getItem("ezRepairSearch");prevAdditionalAction=="true"&&saveModal=="true"&&window.isLoggedIn&&(loadAndOpenModal(),sessionStorage.removeItem("prev_additional_action"),sessionStorage.removeItem("ezRepairSearch"));let currentParams=new URLSearchParams(window.location.search);if(allEasyrepairData.forEach((item,index)=>{let itemCode=item.sku.split("-")[0];item.series_name_list=[];for(let mapping of easyrepairMapping)itemCode===mapping.repair_prod_code&&(item.repair_prod_code=mapping.repair_prod_code,item.repair_type=mapping.repair_type,item.series_name=mapping.series_name,item.series_name_list.some(list=>list===mapping.series_name)||item.series_name_list.push(mapping.series_name))}),currentParams.has("prodCode")){let codeData=(await searchByProductCode(currentParams.get("prodCode"))).data||[],hasResult=document.querySelector("easy-repair-area"),noResult=document.querySelector(".self-repair-result-none-container"),resultSearchKeyword=document.getElementById("result-search-keyword"),easyRepairSearchInput=document.getElementById("easy-repair-search-input");if(codeData.length>0){let tempEasyrepairData=[];codeData.forEach(code=>{const matchingItem=allEasyrepairData.find(item=>item.sku.split("-")[0]===code);matchingItem&&tempEasyrepairData.push(matchingItem)}),allEasyrepairData=tempEasyrepairData,easyRepairSearchInput.value=`${currentParams.get("prodCode")}`,hasResult.classList.remove("hidden"),noResult.classList.add("hidden")}else{hasResult.classList.add("hidden"),noResult.classList.remove("hidden"),resultSearchKeyword.textContent=`${currentParams.get("prodCode")}`,easyRepairSearchInput.value=`${currentParams.get("prodCode")}`;return}}setEasyRepairMO(),showEasyrepairCategory(),handleSelfRepairCategory(),currentParams.has("prodCode")?document.querySelector(".self-repair-content #toggle-parts")&&document.querySelector(".self-repair-content #toggle-parts").classList.add("hidden"):document.querySelector(".self-repair-content #toggle-parts")&&document.querySelector(".self-repair-content #toggle-parts").classList.remove("hidden")});async function searchByProductCode(param){const easyRepairSearch=sessionStorage.getItem("easyRepairSearch");return fetch("https://sidiz-shopify.sidiz.com/v1/easy-repair/mapping",{method:"POST",headers:{"Content-Type":"application/json",Accept:"application/json"},body:JSON.stringify({code:param})}).then(response=>{if(!response.ok)throw new Error("error");return easyRepairSearch&&(window.dataLayer.push({event:"view_search_result",page_type:"\uC81C\uD488 \uCE74\uD14C\uACE0\uB9AC/\uBAA9\uB85D",search_type:"EASY REPAIR_\uAC80\uC0C9",search_term:param,search_result:"Y"}),sessionStorage.removeItem("easyRepairSearch")),response.json()}).catch(error=>(easyRepairSearch&&(window.dataLayer.push({event:"view_search_result",page_type:"\uC81C\uD488 \uCE74\uD14C\uACE0\uB9AC/\uBAA9\uB85D",search_type:"EASY REPAIR_\uAC80\uC0C9",search_term:param,search_result:"N"}),sessionStorage.removeItem("easyRepairSearch")),[]))}function setProductThumbnail(){document.querySelectorAll(".section-common-product-list .content--product").forEach(product=>{let colorchips=product.querySelectorAll(".colorchip");colorchips.forEach((colorchip,idx)=>{colorchip.addEventListener("click",()=>{colorchips.forEach(el=>el.classList.remove("selected")),colorchip.classList.add("selected"),product.querySelectorAll(".image--product").forEach(image=>{image.classList.remove("selected"),image.dataset.id==colorchip.dataset.id&&image.classList.add("selected")})})})})}function handleSelfRepairCategory(){const screenWidth=window.innerWidth,category=document.querySelector(".self-repair-tab_2 .flex-buttons.toggle__content"),categoryClose=document.querySelector(".self-repair-category-close-container"),categoryCloseBtn=document.querySelector(".self-repair-category-close"),categoryOpen=document.querySelector(".self-repair-category-open");category&&categoryClose&&categoryCloseBtn&&categoryOpen&&(screenWidth>1023?(category.classList.remove("hidden"),categoryClose.classList.remove("hidden"),categoryOpen.classList.add("hidden")):(category.classList.add("hidden"),categoryClose.classList.add("hidden"),categoryOpen.classList.remove("hidden")),categoryCloseBtn.addEventListener("click",()=>{category.classList.add("hidden"),categoryClose.classList.add("hidden"),categoryOpen.classList.remove("hidden")}),categoryOpen.addEventListener("click",()=>{category.classList.remove("hidden"),categoryClose.classList.remove("hidden"),categoryOpen.classList.add("hidden")}))}function howtocheckBadgeModal(){const howtocheckBadge=document.querySelector(".easy-repair--search .tag.prod-code-guide");let modalContent=`
		<div class="list-code-modal-container">
			<div class="list-code-modal">
				<div class="list-code-modal-img">
					<img src="${img_product_code}" alt="img_product_ex" />
				</div>
				<div class="list-code-modal-sub-wrapper">
					<div class="list-code-modal-sub">
						<img src="${icon_bulleted_list}" alt="icon_bulleted_list" />
						\uC81C\uD488 \uD558\uBD80\uC5D0 \uBD80\uCC29\uB41C \uD488\uC9C8\uD45C\uC2DC \uC2A4\uD2F0\uCEE4\uC5D0\uC11C \uC81C\uD488 \uCF54\uB4DC\uB97C \uD655\uC778\uD558\uC138\uC694.
					</div>
					<div class="list-code-modal-sub">
						<img src="${icon_bulleted_list}" alt="icon_bulleted_list" />
						\uC81C\uD488 \uCF54\uB4DC\uB294 \uC22B\uC790+\uC601\uBB38\uC73C\uB85C \uAD6C\uC131\uB418\uC5B4 \uC788\uC2B5\uB2C8\uB2E4.
					</div>
				</div>
			</div>
		</div>`;howtocheckBadge.addEventListener("click",()=>{openModalWithContent("\uC81C\uD488 \uCF54\uB4DC \uD655\uC778",modalContent,()=>{document.getElementById("site-alert-modal").classList.add("height-auto--modal");let modalContents=document.querySelector(".modal--contents");modalContents&&modalContents.removeAttribute("style")})})}async function loadAndOpenModal(){const badgeRight=document.querySelector(".easy-repair--search .tag.my-prod-verify");let productData=[],temp="",modalContent=`
		<div class="list-code-modal-container list-my-product-modal">
			<div id="list-my-product" class="list-code-modal">
			</div>
		</div>`;try{if(badgeRight.style.pointerEvents="none",productData=await fetchMyRegisteredProduct(),badgeRight.style.pointerEvents="auto",productData&&productData.length>0){let productFullName2="",representativeImage2="",verifyDate2="";for(const element of productData){const itmCd=element.itmCd,colCd=element.colCd,exactSku=`${itmCd}-${colCd}`;let matchIndex=allData.findIndex(item=>Array.isArray(item.variants)&&item.variants.some(variant=>variant.sku===exactSku));if(matchIndex===-1&&(matchIndex=allData.findIndex(item=>{let itemSku=item.sku&&item.sku.split("-")[0];return itmCd===itemSku})),matchIndex==-1){if(!element.productFullName||element.productFullName.trim()===""){const serialResult=await fetchSerialInfo(element.serialNumber);serialResult&&(element.productFullName=serialResult.itmNm||"")}productFullName2=modifyData("productFullName",element.productFullName),representativeImage2=element.representativeImage&&element.representativeImage!="N/A"?`url('${element.representativeImage}')`:`url('${no_product_image}')`}else productFullName2=modifyData("productFullName",allData[matchIndex].title),representativeImage2=allData[matchIndex].variants[0].image&&allData[matchIndex].variants[0].image!="N/A"?`url('${allData[matchIndex].variants[0].image}')`:`url('${no_product_image}')`;verifyDate2=modifyData("verifyDate",element.verifyDate),temp+=`
					<div class="list-my-product-container" onclick="location.href='/pages/easy-repair?prodCode=${element.itmCd}&tab=ALL'">
				
						<div class="list-my-product-img" style="background-image: ${representativeImage2};">
						</div>
		
						<div class="list-my-product-text">
							<div class="list-my-product-title">${productFullName2}</div>
		
							<div class="list-my-product-text-sub">
								<div class="list-desc">
									<div class="list-left">\uC0C9\uC0C1\uCF54\uB4DC</div>
									<div class="list-right">${element.colCd}</div>
								</div>
								<div class="list-desc">
									<div class="list-left">\uD488\uC9C8\uBCF4\uC99D\uAE30\uAC04</div>
									<div class="list-right">${verifyDate2}\uAE4C\uC9C0</div>
								</div>
								<div class="list-desc">
									<div class="list-left">\uC2DC\uB9AC\uC5BC\uB118\uBC84</div>
									<div class="list-right">${element.serialNumber}</div>
								</div>
							</div>
		
							<div class="list-my-product-text-bottom">
								<div class="list-desc">
									<div class="list-left">\uC81C\uD488\uCF54\uB4DC</div>
									<div class="list-right-code">${element.itmCd}</div>
								</div>
								<div class="list-btn">
									<a href="/pages/easy-repair?prodCode=${element.itmCd}&tab=ALL">\uD638\uD658 \uC81C\uD488 \uBCF4\uAE30</a>
								</div>
							</div>
						</div>
		
					</div>`}temp+='<div class="guide-no-product-btn">\uC815\uD488 \uB4F1\uB85D\uD558\uAE30</div><div style="margin-bottom: 20px;"></div>'}else temp+=`
				<div class="guide-no-product-container">
					<div class="guide-no-product">\uC81C\uD488\uC744 \uB4F1\uB85D\uD558\uACE0 \uC2DC\uB514\uC988\uC758 \uB2E4\uC591\uD55C \uD61C\uD0DD\uACFC \uC9C0\uC6D0\uC744 \uBC1B\uC544\uBCF4\uC138\uC694.</div>
					<div class="guide-no-product-btn">\uC815\uD488 \uB4F1\uB85D\uD558\uAE30</div>
				</div>
			`;openModalWithContent("\uB0B4\uAC00 \uB4F1\uB85D\uD55C \uC81C\uD488 \uCF54\uB4DC",modalContent,()=>{document.getElementById("list-my-product").insertAdjacentHTML("beforeend",temp),document.querySelector(".guide-no-product-btn")&&document.querySelector(".guide-no-product-btn").addEventListener("click",openProductRegisterModal)})}catch(error){console.error(error),badgeRight.style.pointerEvents="auto",temp="",temp+=`
			<div class="guide-no-product-container">
				<div class="guide-no-product">\uC81C\uD488\uC744 \uB4F1\uB85D\uD558\uACE0 \uC2DC\uB514\uC988\uC758 \uB2E4\uC591\uD55C \uD61C\uD0DD\uACFC \uC9C0\uC6D0\uC744 \uBC1B\uC544\uBCF4\uC138\uC694.</div>
				<div class="guide-no-product-btn">\uC815\uD488 \uB4F1\uB85D\uD558\uAE30</div>
			</div>
		`,openModalWithContent("\uB0B4\uAC00 \uB4F1\uB85D\uD55C \uC81C\uD488 \uCF54\uB4DC",modalContent,()=>{document.getElementById("list-my-product").insertAdjacentHTML("beforeend",temp),document.querySelector(".guide-no-product-btn")&&document.querySelector(".guide-no-product-btn").addEventListener("click",openProductRegisterModal)})}}function fetchMyRegisteredProduct(){return openLoadingModal(),fetch("https://sidiz-shopify.sidiz.com/v1/db/customer-prod-verification-list",{method:"POST",headers:{Accept:"application/json","Content-Type":"application/json"},body:JSON.stringify({customerMd5Hash})}).then(response=>response.ok?response.json():response.json().then(error=>{throw new Error(error.response_message||"\uC54C \uC218 \uC5C6\uB294 \uC624\uB958\uAC00 \uBC1C\uC0DD\uD588\uC2B5\uB2C8\uB2E4.")})).finally(()=>{closeLoadingModal()})}function modifyData(name,value){if(name=="productFullName")return!value||value=="N/A"?productFullName="":productFullName=value,productFullName;if(name=="representativeImage")return!value||value=="N/A"?representativeImage="":representativeImage=value,representativeImage;if(name=="verifyDate")return value?verifyDate=value.split("T")[0]:verifyDate="",verifyDate}function showEasyrepairCategory(){let currentURL=new URL(window.location.href),tab="",seriesName="";currentURL.searchParams.has("tab")?tab=currentURL.searchParams.get("tab"):tab="ALL",currentURL.searchParams.has("seriesName")?seriesName=currentURL.searchParams.get("seriesName"):seriesName="ALL";let categoryRepairType=[{title:"\uD5E4\uB4DC\uB808\uC2A4\uD2B8",type:"HR",isView:!1},{title:"\uB4F1\uC88C\uD310",type:"BP",isView:!1},{title:"\uBC14\uD034/\uAE00\uB77C\uC774\uB4DC",type:"ET",isView:!1},{title:"\uD314\uAC78\uC774/\uD314\uAC78\uC774\uD328\uB4DC",type:"AP",isView:!1},{title:"\uAE30\uD0C0\uBD80\uD488",type:"ETC",isView:!1}];allEasyrepairData.forEach(item=>{item.repair_type&&categoryRepairType.forEach(category=>{if(category.type===item.repair_type){category.isView=!0;return}})});let htmlContent_1=`
		<div class="card card--no-borders card--animation active" data-tab1="ALL">
			<div class="text__problem">
				<h2 class="self-repair-tab-text">\uC804\uCCB4</h2>
			</div>
		</div>
	`;categoryRepairType.forEach(category=>{category.isView&&(htmlContent_1+=`
			 <div class="card card--no-borders card--animation" data-tab1="${category.type}">
          <div class="text__problem">
            <h2 class="self-repair-tab-text">${category.title}</h2>
          </div>
        </div>
			`)});let easyRepairTab_1=document.getElementById("easy-repair-tab-1");easyRepairTab_1.replaceChildren(),easyRepairTab_1.insertAdjacentHTML("beforeend",htmlContent_1);let categorySeriesNameSet=new Set;allEasyrepairData.forEach(item=>{Array.isArray(item.series_name_list)&&item.series_name_list.length>0?item.series_name_list.forEach(seriesName2=>{seriesName2&&seriesName2!=="ALL"&&categorySeriesNameSet.add(seriesName2)}):item.series_name&&item.series_name!=="ALL"&&categorySeriesNameSet.add(item.series_name)});let categorySeriesName=Array.from(categorySeriesNameSet);categorySeriesName.sort((a,b)=>b.localeCompare(a,"ko",{numeric:!0,sensitivity:"base"}));let htmlContent_2=`
		<div class="self-repair-tab_2-item card active" data-tab2="ALL">
			\uC804\uCCB4
		</div>
	`;categorySeriesName.forEach(category=>{htmlContent_2+=`
			<div class="self-repair-tab_2-item card" data-tab2="${category}">
				${category}
			</div>
		`});let easyRepairTab_2=document.getElementById("easy-repair-tab-2");easyRepairTab_2.replaceChildren(),easyRepairTab_2.insertAdjacentHTML("beforeend",htmlContent_2);let repairTypeList=document.querySelectorAll("div[data-tab1]"),seriesNameList=document.querySelectorAll("div[data-tab2]");repairTypeList.forEach(repairTypeItem=>{repairTypeItem.dataset.tab1==tab?repairTypeItem.classList.add("active"):repairTypeItem.classList.remove("active"),repairTypeItem.addEventListener("click",()=>{currentURL.searchParams.has("tab")?currentURL.searchParams.set("tab",repairTypeItem.dataset.tab1):currentURL.searchParams.append("tab",repairTypeItem.dataset.tab1),window.location.href=currentURL.toString()})}),seriesNameList.forEach(seriesNameItem=>{seriesNameItem.dataset.tab2==seriesName?seriesNameItem.classList.add("active"):seriesNameItem.classList.remove("active"),seriesNameItem.addEventListener("click",()=>{currentURL.searchParams.has("seriesName")?currentURL.searchParams.set("seriesName",seriesNameItem.dataset.tab2):currentURL.searchParams.append("seriesName",seriesNameItem.dataset.tab2),window.location.href=currentURL.toString()})}),currentURL.searchParams.has("prodCode")||(tab&&tab!="ALL"&&seriesNameList.forEach(item=>{let tabValue=item.getAttribute("data-tab2");tabValue!=="ALL"&&(allEasyrepairData.some(data=>data.repair_type==tab&&data.series_name_list.some(list=>list===tabValue))?item.classList.remove("hidden"):item.classList.add("hidden"))}),seriesName&&seriesName!="ALL"&&repairTypeList.forEach(item=>{let tabValue=item.getAttribute("data-tab1");tabValue!=="ALL"&&(allEasyrepairData.some(data=>data.series_name_list.some(list=>list===seriesName)&&data.repair_type==tabValue)?item.classList.remove("hidden"):item.classList.add("hidden"))})),currentURL.searchParams.has("prodCode")?tab!=="ALL"&&(allEasyrepairData=allEasyrepairData.filter(item=>item.repair_type===tab)):(tab==="ALL"&&seriesName==="ALL"||(allEasyrepairData=allEasyrepairData.filter(item=>tab==="ET"?item.repair_type==="ET":(tab==="ALL"||item.repair_type===tab)&&(seriesName==="ALL"||item.series_name_list.some(list=>list===seriesName)))),tab==="ET"&&document.querySelectorAll(".self-repair-tab_2-item").forEach(el=>{el.dataset.tab2=="ALL"?(el.classList.remove("hidden"),el.classList.add("active")):(el.classList.add("hidden"),el.classList.remove("active"))})),showEasyrepair(allEasyrepairData),setProductThumbnail(),handleDataTable(allEasyrepairData.length)}function showEasyrepair(product_list){let productContainer=document.querySelector(".self-repair-content").querySelector(".showEasyrepair");if(!(!product_list||product_list.length==0)){productContainer.replaceChildren();for(let product of product_list){let inventory=!1;for(let variant of product.variants){if(variant.inventory_quantity===void 0||variant.inventory_quantity===null){inventory=!0;break}if(variant.inventory_quantity>0){inventory=!0;break}}product.inventory=inventory}product_list.forEach((product,index)=>{let currentDate=Math.floor(Date.now()/1e3),publishedDate=Math.floor(new Date(product.published_at).getTime()/1e3),fiveDaysInSeconds=7200*60,newThreshold=publishedDate+fiveDaysInSeconds,variantData=product.variants[0],price_varies=product.price_varies,price=variantData.price,specialPrice=variantData.special_price,eventStartDate=variantData.event_start_dt,eventEndDate=variantData.event_end_dt,customerDiscountRate=0,isEvent=!1,priceTag="";if(eventStartDate&&eventEndDate){const now=new Date,start=new Date(eventStartDate),end=new Date(eventEndDate);now>=start&&now<=end&&(isEvent=!0)}if(priceTag=`
      <div class="text--price">
        <span class="price--cur">${Number(price).toLocaleString()}\uC6D0${price_varies=="true"?"~":""}</span>
      </div>
    `,isEvent){let priceNum=parseFloat(price.replace(/,/g,"")),specialPriceNum=parseFloat(specialPrice.replace(/,/g,""));priceNum>specialPriceNum&&(customerDiscountRate=Math.round((priceNum-specialPriceNum)/priceNum*100),customerDiscountRate=parseInt(customerDiscountRate,10),priceTag=`
					<div class="title--discount">\uD68C\uC6D0 \uD560\uC778\uAC00</div>
          <div class="text--price">
            <span class="percent--discount">${customerDiscountRate}%</span>
            <span class="price--cur">${specialPriceNum.toLocaleString()}\uC6D0${price_varies=="true"?"~":""}</span>
            <div class="price--prev">${priceNum.toLocaleString()}\uC6D0${price_varies=="true"?"~":""}</div>
          </div>
        `)}let badgeList=product.badge_list,badge_html="";badgeList&&badgeList.length>0&&badgeList.forEach(badge=>{if(!(currentDate<newThreshold&&badge.handle=="new")){let text_color=badge.text_color||"#000000",background_color=badge.background_color||"#ffffff",border_color=badge.border_color||"#d6dade";badge_html+=`
					<div class="product-badge" data-badge="${badge.handle}" style="color: ${text_color}; background-color: ${background_color}; border: 1px solid ${border_color};">
						${badge.text}
					</div>
					`}});let series_name_list="";product.series_name_list&&(series_name_list=product.series_name_list.join(",")+",");const listCardDesc=formatListCardDesc(product.list_card_desc);let temp=`
			<tr 
				class="item-list" 
				data-series_name="${product.series_name?product.series_name:""}" 
				data-series_name_list="${series_name_list}" 
				data-repair_type="${product.repair_type?product.repair_type:""}"
			>
				<td>
					<div id="product-${product.id}" class="content--product" data-index="${index+1}">
						<div class="header--product" data-skulist="">
							<div class="wrapper--image">
								${(()=>{let image="";return product.variants.forEach((variant,index2)=>{image+=`
											<div class="image--product ${index2===0?"selected":""}" data-id="${variant.id}">
												${variant.featured_image.src_tag}
											</div>
										`}),image})()}
							</div>

							<div class="wrapper--badge">
								${currentDate<newThreshold?'<div class="product-badge" data-badge="new">NEW</div>':""}
								${badge_html}
							</div>

							<div class="button--like" data-item-category="${product.category}" data-item-name="${product.title}" data-item-img="${product.variants[0].featured_image.src}">
								<img src="${icon_bookmark_line_bk_28}" alt="\uBD81\uB9C8\uD06C \uC544\uC774\uCF58" width="28" height="28"
										data-bookmark="false" data-id="${product.id}" data-handle="${product.handle}" 
										onclick="addBookmark(event.target)" class="bookmark-false">
								<img src="${icon_bookmark_blue}" alt="\uBD81\uB9C8\uD06C \uC544\uC774\uCF58" width="28" height="28"
										data-bookmark="true" data-id="${product.id}" data-handle="${product.handle}" 
										onclick="removeBookmark(event.target)" class="bookmark-true hidden"> 
							</div>
							<a href="${product.url}"></a>
					</div>

					<div class="body--product">
							<div class="title--product"><a href="${product.url}">${product.title}</a></div>
							<div class="price--product">
								${priceTag}
							</div>
							<div class="color--product">
								${(()=>{let color="";return product.variants.forEach((variant,index2)=>{color+=`
											<div class="colorchip ${index2===0?"selected":""}" data-id="${variant.id}">
												<div class="color" style="background-color: ${variant.color_rgb};"></div>
											</div>
										`}),color})()}
								</div>
								${product.inventory?"":'<div class="inventory--product">\uC77C\uC2DC\uD488\uC808</div>'}
								${listCardDesc?`<div class="description--product">${listCardDesc}</div>`:""}
							</div>
						</div>
					</td>
			</tr>
    `;productContainer.insertAdjacentHTML("beforeend",temp)})}}let debounceTimeout,previousPageLength=window.innerWidth<1024?20:42;function handleDataTable(dataLength){window.addEventListener("resize",function(){clearTimeout(debounceTimeout),debounceTimeout=setTimeout(adjustTableLength,200)});function adjustTableLength(){let pageLength2=window.innerWidth<1024?20:42;pageLength2!=previousPageLength&&(product_table.page.len(pageLength2).draw(),previousPageLength=pageLength2)}let pageLength=window.innerWidth<1024?20:42,navigationEntries=performance.getEntriesByType("navigation");navigationEntries.length>0&&navigationEntries[0].type!=="back_forward"&&localStorage.removeItem("DataTables_product_table_/pages/easy-repair"),product_table=$("#product_table").DataTable({paging:!0,lengthChange:!1,searching:!0,order:[],info:!1,autoWidth:!1,pagingType:"simple_numbers",pageLength,stateSave:!0,language:{emptyTable:"\uD574\uB2F9\uD558\uB294 \uC81C\uD488\uC774 \uC5C6\uC2B5\uB2C8\uB2E4.",infoEmpty:"\uD574\uB2F9\uD558\uB294 \uC81C\uD488\uC774 \uC5C6\uC2B5\uB2C8\uB2E4.",paginate:{previous:`<img src="${icon_left_line_bk}" alt="icon_left_line_bk" width="22" height="22">`,next:`<img src="${icon_right_line_bk}" alt="icon_right_line_bk" width="22" height="22">`}}});let dataPagination=document.querySelector(".self-repair-content .dt-paging.paging_simple_numbers");dataLength==0?dataPagination&&dataPagination.classList.add("hidden"):dataPagination&&dataPagination.classList.remove("hidden"),$("#product_table").on("page.dt",function(){setTimeout(function(){if(dataPagination){let tableOffset=document.querySelector("#product_table").getBoundingClientRect().top+window.pageYOffset,viewportHeight=window.innerHeight,scrollTarget=tableOffset-viewportHeight/3;window.scrollTo({top:scrollTarget,behavior:"smooth"})}},100)})}function addClickSearchEvent(){let searchTerm=document.getElementById("easy-repair-search-input").value,clickType=document.querySelector("#easy-repair-tab-1 > div.active").innerText,clickText=this.querySelector(".title--product a").innerText,clickUrl=this.querySelector(".title--product a").href;window.dataLayer.push({event:"click_search_result",page_type:window.pageType,search_type:"EASY REPAIR_\uAC80\uC0C9",search_term:searchTerm,click_type:clickType,click_text:clickText,click_url:clickUrl})}function setEasyRepairMO(){if(new URLSearchParams(window.location.search).has("prodCode")){const observer=new MutationObserver(mutations=>{mutations.forEach(mutation=>{mutation.type==="childList"&&mutation.addedNodes.forEach(node=>{node.nodeType===Node.ELEMENT_NODE&&node.addEventListener("click",addClickSearchEvent)})})}),table=document.querySelector(".showEasyrepair");observer.observe(table,{childList:!0,subtree:!0})}}
//# sourceMappingURL=/cdn/shop/t/152/assets/self-repair-search.js.map
