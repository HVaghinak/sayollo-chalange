## Run with Docker-compose
- cd sayollo (root of the project)
- docker-compose build
- docker-compose up -d 

## Run with local env
- cd sayollo (root of the project)
- pip install pipenv
- pipenv install --dev
- pipenv run flask run

## Test
- pipenv run pytest

## Usage
- API: POST - http://localhost:8080/ads/
    The api accepts JSON object and returns XML object. During that process it sends a request to an external API and returns the received Response. Store Requests count per User and SDK VERSION
    <details>
        <summary>JSON example</summary>
    <p>
  
    ```json
        {
          "country_code": "DE",
          "platform": "Sayollo",
          "session_id": "123456",
          "sdk_version": "1.00.1",
          "username": "test_user"
        }
    ```
    </p>
    </details>

    <details> <summary> Response of API </summary>
        
    ```xml
    <VAST xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" version="2.0">
    <Ad>
        <InLine>
            <Error>
                <![CDATA[]]>
            </Error>
            <Creatives>
                <Creative>
                    <Linear>
                        <Duration>00:00:06</Duration>
                        <MediaFiles>
                            <MediaFile>
                                <![CDATA[https://sayollo.nyc3.digitaloceanspaces.com/Covid4.webm]]>
                            </MediaFile>
                        </MediaFiles>
                        <TrackingEvents />
                    </Linear>
                </Creative>
            </Creatives>
        </InLine>
    </Ad>
  </VAST>
    ```
    </details>

- API: POST - http://localhost:8080/impressions/
    The api accepts JSON object and returns XML object. Store Impressions count per User and SDK VERSION
    <details>
        <summary>JSON example</summary>
    <p>
  
    ```json
        {
          "country_code": "DE",
          "platform": "Sayollo",
          "session_id": "123456",
          "sdk_version": "1.00.1",
          "username": "test_user"
        }
    ```
    </p>
    </details>

    <details> <summary> Response of API </summary>
      ""
    </details>

## TODOs
- Add Nginx as HTTP Proxy server on the top of Gunicorn
- Implement Tests
- Check for "#TODO"-s in the code to find out the points which needs to be changed/improved
