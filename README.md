# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution:  
> tokenB->tokenA amountIn = 5, amountOut = 5.655321988655322  
> tokenA->tokenD amountIn = 5.655321988655322, amountOut = 2.4587813170979333  
> tokenD->tokenC amountIn = 2.4587813170979333, amountOut = 5.0889272933015155  
> tokenC->tokenB amountIn = 5.0889272933015155, amountOut = 20.129888944077443  
> final reward = 20.129888944077443

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution:  
在自動做市商（AMM）中，slippage是指在執行交易時，交易價格與交易執行之間的差異。這種差異通常是pool中可用的流動性不足而導致的。例如，如果在一個流動性較低的pool中購買大量資產，可能會導致交易價格短時間出現大量變動，進而造成slippage。  
Uniswap利用了一種稱為“恆定乘積”的函數來解決這個問題。該函數通過在資金池中保持資產數量的乘積不變來確保相對穩定的價格。具體來說，Uniswap V2的恆定乘積函數可以用以下方式表示： x * y = k, 其中，k為定值。  

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution:  
1. 防止塵埃攻擊：扣除最小流動性量有助於防止塵埃攻擊。塵埃攻擊涉及添加微小量的流動性到一個pool中，以操縱價格使得攻擊者獲益。通過要求添加一定量的流動性，協議確保只有顯著數量的流動性被添加到池中，使其不容易受到操縱。  
  
2. 確保足夠的流動性深度：要求添加最小流動性量有助於確保池中的流動性深度達到一定的閾值。因為有更多的流動性可用於吸收大宗交易而不會對價格產生顯著影響，而更深的流動性池通常提供更好的交易體驗。  


## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution:  
1. 維持恆定乘積：Uniswap V2使用恒定乘積函數來維持資金池中資產數量的乘積不變。通過使用特定的公式來獲得流動性，可以確保每次添加流動性後，乘積仍然保持不變。這有助於維持恒定乘積的特性，從而確保交易的有效性和可預測性。  
  
2. 防止操縱：限制僅使用特定公式來獲得流動性可以防止操縱資金池的企圖。如果允許任意添加流動性，可能會導致某些交易者試圖通過不當手段來影響資金池中的價格。通過強制使用特定公式，可以降低此類攻擊的風險。  


## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution:  
sandwich attack是一種DEX中常見的攻擊手法，旨在從交易者身上獲利。這種攻擊通常發生在流動性較低的交易pair上，攻擊者可以通過兩個交易來進行攻擊。  
  
sandwich attack的運作方式如下：首先，攻擊者會觀察一個特定的交易對，並選定一個交易。然後，攻擊者會在這個交易之前和之後迅速發起自己的交易。在這兩個交易中，攻擊者會將價格推向有利於自己的方向，進而影響到交易者的成交價格。  

