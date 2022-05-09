# Topological Image modification for object detection and topological image processing of skin lesions

- Author: Robin Vandaele, Guillaume Adrien Nervo, Olivier Gevaert

- Read: 2022년 5월 9일

- Subject: Topological Data Analysis, Computer Vision, Image Processing, Object Detection

- Submit: 2020년 12월 3일

- URL: https://www.nature.com/articles/s41598-020-77933-y

# Summary

- **ISSUE** : 이미지에서 무관한 정보를 버리고 적절한 영역 내의 중요한 오브젝트를 식별하게 하고 싶다.
- **SOLUTION** : 이미지 데이터의 Persistent homology에서 적절한 threshold를 선택하는 것으로 무관한 object를 파괴한 뒤, topological property에 따라 해당 영역을 매꿈.


# Main Idea

이 논문의 핵심 아이디어는 *topologically significant하지만 irrelevant한 object를 제거*하는 것이다.
이 아이디어는 중요한 object는 적어도 이미지의 테두리에 위치해있지 않다는 가정으로부터 나온다.
그러므로 이미지의 테두리 부분에 가장 낮은 pixel 값을 부여해줘서 filtration을 만들어, background와 같은 정보들은 테두리의 homology class에 merging해 infinite persistence를 가지도록 만든다. 
이렇게 되면 상당히 많은 irrelevant한 object들이 topologically significant 해진다.
이제 이들을 제외하고 finite persistence만 가지는 object만 고려한 뒤, thresholding으로 적당한 persistence 이상을 가지는 영역만 고려하면 중요한 object를 걸러낼 수 있게 된다.
단순히 *topologically insignificant*한 object만 제거하던 기존의 아이디어와 다름에 유의하자.


# Motivation

Image data는 특유의 grid structure 덕분에 TDA를 수행하기 용이하다.
그러나 실제 이미지 내에는 outlier가 많기 때문에 단순히 persistent homology를 사용하는 것으로 원하는 solution을 얻기 어렵다.
저자들은 이런 상황을 극복하고자 *Topological Image Modification (TIM)*을 이용해 먼저 이미지를 TDA를 하기 좋게끔 처리한다음 *Topological Image Processing (TIP)*으로 원하는 작업을 수행한다.
TIM과 TIP의 


# Methodology
## 1. Persistent homology of images
Persistent homology에 대한 이론은 생략한다. 
여기서는 일반적으로 TDA에서 이미지 데이터를 다룰때 사용하는 *Cubical complex*를 사용하지 않고 *Simplicial complex*를 사용한다. 
Cubical complex를 사용할 때는 pixel이 상하좌우 네 가지 방향으로만 연결될 수 있다.
그러나 Simplicial complex를 사용하는 경우에는 pixel이 여덟 가지 방향으로 연결될 수 있다.

개인적인 의견으로 Simplicial complex가 Cubical complex가 더 디테일한 연결성을 표현할 수 있을진 몰라도 complex를 구성하는 component가 cubical에 비해 월등히 많기 때문에 complexity 면에서 불리하다.
애초에 TDA로 데이터 처리하는 것이 그다지 빠르지 못한데, 이러한 점은 매우 불리하게 작용할 것으로 보인다.
더군다나 image의 resolution이 충분히 커지면 cubical complex를 쓰는 것으로 충분히 detail한 정보를 캐치할 수 있을 것으로 보인다.

어떤 경우던 상관없이 이미지 I에서 filtration을 구성하기 위해 $f(\sigma) = \max_{p\in\sigma} gray_I(p)$를 사용한다. 
여기서 $\sigma$는 이미지의 grid 위에 정의된 simplicial (또는 cubical) complex $K$다. 
이 함수는 simplex (혹은 k-cube)를 구성하는 pixel들 중 가장 grayscale 값이 큰 값으로 simplex에 값을 부여하는 것이다.
이 함수 $f$를 사용하여 sublevel set filtration $\empty = K_0 \subseteq K_1 \subseteq \ldots \subseteq K_n = K$를 구성한다. 

RGB 이미지의 경우앤 standard linear converter를 사용하여 다음과 같이 grayscale화 한다:
$gray_I(p) = \frac{1}{1000} (299 red_I(p) + 587 green_I(p) + 114 blue_I(p))$

standard linear converter는 Python PIL 라이브러리에 구현되어 있다.

